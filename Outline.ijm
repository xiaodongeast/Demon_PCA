// change all the current selections into the bands
// xiaodong @ Gannon Lab
w=getWidth();
h=getHeight();
count=roiManager("count");
for (ii=0;ii<count;ii++)
{roiManager("select",ii);
run("Make Band...", "band=2.03"); // change band size to the desired number
}

newImage("showResult.tif", "8-bit black", w, h,1);
selectWindow("showResult.tif");

for (ii=0;ii<count;ii++)
{roiManager("select",ii);
run("Fill");
write(ii);
}
write("done!!!");