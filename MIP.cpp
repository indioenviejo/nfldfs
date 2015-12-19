#include "stdio.h"
#include "stdlib.h"
#include "glpk.h"
#include "stdio.h"
#include "glpk.h"
#include <stdio.h>      
#include <stdlib.h>     
#include <string>
#include <sstream>
/*
Maximize
 obj: x1 + 2 x2 + 3 x3 + x4
Subject To
 c1: - x1 + x2 + x3 + 10 x4 <= 20
 c2: x1 - 3 x2 + x3 <= 30
 c3: x2 - 3.5 x4 = 0
Bounds
 0 <= x1 <= 40
 2 <= x4 <= 3
General
 x4
End
*/

int main(void)
{
  glp_prob *mip = glp_create_prob();
  glp_set_prob_name(mip, "DFF");
  glp_set_obj_dir(mip, GLP_MAX);

  glp_add_rows(mip, 5);
  glp_set_row_name(mip, 1, "QB");
  glp_set_row_bnds(mip, 1, GLP_DB, 0.0, 1.0);
  glp_set_row_name(mip, 2, "RB");
  glp_set_row_bnds(mip, 2, GLP_DB, 0.0, 2.0);
  glp_set_row_name(mip, 3, "TE");
  glp_set_row_bnds(mip, 3, GLP_DB, 0.0, 1.0);
  glp_set_row_name(mip, 4, "WR");
  glp_set_row_bnds(mip, 4, GLP_DB, 0.0, 4.0);
  glp_set_row_name(mip, 5, "Cost");
  glp_set_row_bnds(mip, 5, GLP_DB, 0.0, 45800.0);  
  
  int numPlayers = 126;
  glp_add_cols(mip, numPlayers); // No. of players + 1

  FILE *myfile;
  double myvariable;
  int i;
  myfile=fopen("/home/raghav/mygithub/nfldfs/week15coeff.csv", "r");
  for (i = 0 ; i < numPlayers; i++)
  {
    fscanf(myfile,"%lf",&myvariable);
    printf("%.4f\n ",myvariable);
    printf("%d\n ",i);
    std::stringstream s;
    s << "x" << i+1;
    glp_set_col_name(mip, i+1, s.str().c_str());
    glp_set_col_bnds(mip, i+1, GLP_DB, 0.0, 1.0);
    glp_set_obj_coef(mip, i+1, myvariable);
  }
  
  
    int ia[1+252], ja[1+252];
    double ar[1+252];int j;

    //# Constraint 1 condition :QB
    int counter = 1;
    for (j = 1 ; j<=33 ;++j)
    {
        ia[counter] = 1;
        ja[counter] = j;
        ar[counter] = 1;
        counter = counter +1;
    }
    
    //# Constraint 2 condition : RB
    for (j = 34 ; j<=63 ;++j)
    {
        ia[counter] = 2;
        ja[counter] = j;
        ar[counter] = 1;
        counter = counter +1;
    }

    //# Constraint 3 condition : TE
    for (j = 64 ; j<=76;++j)
    {
        ia[counter] = 3;
        ja[counter] = j;
        ar[counter] = 1;
        counter = counter +1;
    }

    //# Constraint 4 condition : WR
    for (j = 77 ; j<=126 ;++j)
    {
        ia[counter] = 4;
        ja[counter] = j;
        ar[counter] = 1;
        counter = counter +1;
    }    
    
  myfile=fopen("/home/raghav/mygithub/nfldfs/week15sals.csv", "r");
  printf("%d\n ",counter);
  printf("-------------------------\n");
  for (j = 1 ; j <= 126; j++)
  {
      fscanf(myfile,"%lf",&myvariable);
      printf("%.4f\n ",myvariable);
      ia[counter] = 5;
      ja[counter] = j;
      ar[counter] = myvariable;
      counter = counter +1;
      printf("%d\n ",counter);
      printf("-------------------------\n");
  }    
    
  glp_load_matrix(mip, 252, ia, ja, ar);

  glp_iocp parm;
  glp_init_iocp(&parm);
  parm.presolve = GLP_ON;
  int err = glp_intopt(mip, &parm);
    

  double z = glp_mip_obj_val(mip);
  printf("teamValue : %\lf\n  was selected",z);
  for (j = 1 ; j<= 126 ; ++j)
  {
  double x1 = glp_mip_col_val(mip, j);
  if (x1 > 0)
   printf("%lf\t%d \n",x1,j);
  }
   
  glp_delete_prob(mip);
  return 0;
}
