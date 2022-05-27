# A206
import math

tax_included:int = int(input());
tax_included = math.floor(tax_included * 1.08);
if(tax_included < 206):
  print("Yay!");
elif(tax_included > 206):
  print(":(");
elif(tax_included == 206):
  print("so-so");
