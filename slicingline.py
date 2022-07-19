line = "MyBW.WARS06_WMS_vs0"
strpos = line.find("_")
endpos = line.find("vs0")
trans_code = line[strpos+1:endpos-1]
print (trans_code)