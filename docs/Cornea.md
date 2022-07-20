# Building the Cornea Lens
![Screen Shot 2022-07-20 at 4 19 14 PM](https://user-images.githubusercontent.com/106686527/180092380-f10ce813-1b9f-4448-84f9-24748df6da06.png)![Screen Shot 2022-07-20 at 4 19 40 PM](https://user-images.githubusercontent.com/106686527/180092392-51654629-b9c2-4ea2-9b93-f650ead6d8ac.png)![Screen Shot 2022-07-20 at 4 20 01 PM](https://user-images.githubusercontent.com/106686527/180092414-2a3f1ad7-a5b7-4798-916e-ebc7ab992e7c.png)![Screen Shot 2022-07-20 at 4 20 07 PM](https://user-images.githubusercontent.com/106686527/180092438-157d640b-deee-454f-a696-77da98313bbc.png)
## Download Blender
![image](https://user-images.githubusercontent.com/106686527/175160863-447fe426-adad-4917-9e5c-40c116f97815.png)
https://www.blender.org
- Blender is a free, open-source software where you can build 3D models, shade them, and even later animate your creation! Because of how powerful it is and its many different types of lights, we will be using Blender in our project. Plus, it has a monkey! To download Blender, click on the link above and follow the website's instructions. If you want a general guide to how to use Blender, they also have a YouTube playlist where they walk you through the fundamentals on how to use their software. Simply search "Blender fundamentals" into Youtube. The playlist should be the first result, below the ad of course. 
## Draw Two Spheres
- Delete the default cube
- In the upper left, click on “Add” -> “Mesh” -> “UV Sphere”
![Screen Shot 2022-06-26 at 9 15 06 PM](https://user-images.githubusercontent.com/106686527/175853356-c4f0c47f-7a15-4c3f-a707-64780ea89340.png)
- Right click on the sphere and select “Shade Smooth.” 

![image](https://user-images.githubusercontent.com/106686527/175162483-df87b2a9-f054-40c7-a0fd-f87084594043.png)

- Press Ctrl+C, then Ctrl+V to get an identical sphere in the same spot (the only difference you will likely see is that the sphere is highlighted in a darker orange; this is fine both spheres are present, but just in the same location, making it look like one sphere).
- Go to the menu in the upper right corner and select one of the spheres (it doesn’t matter which one). 
- On the sphere that you have selected go down to the “Scale” section of the object properties tab and make it so that all X-Y-Z are set to 0.783, or our radius of curvature for the anterior surface of the cornea (we are also scaling a millimeter to a decimeter so that it is easier for us to see our product in Blender.
- Now, click on the sphere that you haven’t changed, go to the object properties tab again if you aren’t already there (the orange square), and set all of the X-Y-Z scale to 0.65, or our posterior radius of curvature.
![Screen Shot 2022-07-20 at 9 41 09 AM](https://user-images.githubusercontent.com/106686527/180087480-2392ed94-ce14-4cc0-8b02-47f09d61228d.png)
## Orient Spheres
- Set your viewport shading to “Wireframe” ![image](https://user-images.githubusercontent.com/106686527/180087613-caaca5f0-9be6-42c9-bc5c-0164a8b734f5.png).
- Orient yourself so that you are facing the spheres dead-on, and therefore see two circles (I found that clicking on the -Y ball in the upper right cartesian tool![image](https://user-images.githubusercontent.com/106686527/180087894-173a0149-d74d-4c40-96a6-3a5a1b368dce.png)
 works best for me).
![Screen Shot 2022-07-20 at 9 43 59 AM](https://user-images.githubusercontent.com/106686527/180087417-ee88d85e-6e1c-4e2c-ac0f-4af1cb96062f.png)
- Click on the “Measure” tool on the left, the one with two rulers.![image](https://user-images.githubusercontent.com/106686527/180087549-529f2c22-6af0-407e-8eb4-2c1e8d198e73.png)
- On the right most edge of the sphere that touches the horizontal axis in your view, click on the edge of the sphere and drag until you are in the 0.054-0.055 range, then unclick. It is tricky to get to that small of a number, so I suggest praying and zooming in.
![Screen Shot 2022-07-20 at 9 51 21 AM](https://user-images.githubusercontent.com/106686527/180088037-ccba5a8f-b0b1-4ce2-a879-ac2816991076.png)
- Once you get that measurement, you may notice that the little window that tells you the measurement is hiding where exactly it starts and stops, so move your mouse to the right half of the measurement, the edge of the sphere, and click and drag that part away. This way, we can see exactly where we ended (since we already know where we started: the edge of the sphere).
- Now, move the right-most part of the smaller sphere to where the measurement ended. If you try to move the sphere through the “Move” tool on the left, you’ll notice that our measurement goes away, so instead, I suggest going down to “Object Properties” on the right, and sliding the “Location X” tab until the sphere is where you want it. You can delete the measurement now by clicking on it and pressing X, then clicking on “Delete” if you would like.
![Screen Shot 2022-07-20 at 9 59 23 AM](https://user-images.githubusercontent.com/106686527/180088109-cb567b96-6b68-4704-96be-5c11fc783755.png)
## Measure and Cut Out Cornea: Height
### Anterior/Front
- Click on the measure tool again, and start your measurement in the center between the two spheres on the right and on the horizontal axis; it’s fine if it’s not perfectly in the center. Now, drag up until you hit 0.3; our cornea will have a diameter of about 9 mm.
![Screen Shot 2022-07-20 at 10 08 09 AM](https://user-images.githubusercontent.com/106686527/180088381-f81c075b-72dc-41f8-8ed9-f70f068d7e24.png)
- To make our lives easier, make note of the line above the measurement. For example, mine is the second line above the horizontal axis. You will want to do this so that you can ensure symmetry (so I will make note of the second line below the horizontal axis).
- Now, click on the outer sphere and go into “Edit Mode” by clicking on the drop down menu in the upper left that right now says “Object Mode”.
- Click away from the sphere to deselect it.
- Next to the drop down menu in the upper left there will be three cubes. Click on the right most cube, so that you are only selecting the faces of the sphere.
- Now, highlight the faces that are above and below the lines that you have made note of respectively.
![Screen Shot 2022-07-20 at 10 46 26 AM](https://user-images.githubusercontent.com/106686527/180088477-898f64cc-36dc-48e8-b217-d7cf24ca4a7e.png)
- Delete these faces by pressing X, then clicking delete “Faces.”
![Screen Shot 2022-07-20 at 10 48 15 AM](https://user-images.githubusercontent.com/106686527/180088530-41313f45-642c-4632-8012-05c0f2b74591.png)
### Posterior/Back
- Switch back into object mode and select the sphere still intact and go back into “Edit Mode” by clicking on the drop down menu in the upper left that right now says “Object Mode”.
- Click away from the sphere to deselect it.
- On the left-hand side, click on the “Loop Cut” tool![image](https://user-images.githubusercontent.com/106686527/180088808-0930613c-e8b5-407a-b5d8-5110d6de00cf.png)
 and create cuts that are along the edge of your cut sphere by clicking when the yellow line is horizontal and in the relative area where you want the cut to be. If you need to move the cuts, just click and hold, then drag the cut to where you want it to be.
 
![Screen Shot 2022-07-20 at 10 50 49 AM](https://user-images.githubusercontent.com/106686527/180089290-31767177-4d96-493e-9ca7-2cf938822278.png)![Screen Shot 2022-07-20 at 10 51 09 AM](https://user-images.githubusercontent.com/106686527/180089318-2f07b7bd-1b3b-4fa8-976c-e4c535f361c2.png)

- Next to the drop down menu in the upper left there will be three cubes. Click on the right most cube![image](https://user-images.githubusercontent.com/106686527/180089190-3bf23888-899a-4781-8a2b-e89871e81363.png), so that you are only selecting the faces of the sphere.
- Now, highlight the faces that are above and below the cuts that you have made respectively.
![Screen Shot 2022-07-20 at 10 55 45 AM](https://user-images.githubusercontent.com/106686527/180089421-51e8a3b1-0962-42f6-a1e1-163af911c702.png)
- Delete these faces by pressing X, then clicking delete “Faces.”
![Screen Shot 2022-07-20 at 10 56 02 AM](https://user-images.githubusercontent.com/106686527/180089726-65ed730c-fa04-4822-95f1-4295c6a96013.png)
## Measure and Cut Out Cornea: Width
### Anterior/Front
- Orient yourself so that you’re now facing the right side where we focused all our measurements on (for me, I clicked on the X ball on the cartesian tool in the upper right).
- Use the measure tool, and start the measurement at the center of the lens, then drag horizontally until you reach 0.3.
![Screen Shot 2022-07-20 at 11 07 12 AM](https://user-images.githubusercontent.com/106686527/180089880-e5658bb1-cfc6-42a6-98b1-72b3a5d8d8af.png)
- Again, make note of the next line to your measurement and do the same for the other side. If you are getting confused with which line goes to which sphere, you can hide the inner sphere by going to the upper right where there is an array of your objects and clicking on the eye symbol next to the inner sphere. For me, this line is the third one from the vertical axis.
- Now, click on the outer sphere and go into “Edit Mode” by clicking on the drop down menu in the upper left that right now says “Object Mode”.
- Click away from the sphere to deselect it.
- Next to the drop down menu in the upper left there will be three cubes. Click on the right most cube ![image](https://user-images.githubusercontent.com/106686527/180089190-3bf23888-899a-4781-8a2b-e89871e81363.png), so that you are only selecting the faces of the sphere.
- Now, highlight the faces that are above and below the lines that you have made note of respectively.
![Screen Shot 2022-07-20 at 11 08 08 AM](https://user-images.githubusercontent.com/106686527/180090140-781fca9b-77fe-4dd7-a9e3-a7a5ef66c5b1.png)
- Delete these faces by pressing X, then clicking delete “Faces.”
- ![Screen Shot 2022-07-20 at 11 12 26 AM](https://user-images.githubusercontent.com/106686527/180090298-85e9efd8-238b-40da-a0fe-bd7d02ebc43f.png)
- If you rotate your view, you may notice that there are faces on the other side that weren’t deleted. Delete these faces individually.
![Screen Shot 2022-07-20 at 11 16 18 AM](https://user-images.githubusercontent.com/106686527/180091782-a5571a03-a29a-42c2-99f9-0ad1c963b1b9.png)
### Posterior/Back
- Switch back into object mode and select the sphere still intact and go back into “Edit Mode” by clicking on the drop down menu in the upper left that right now says “Object Mode”. (Make sure to bring it back into view by clicking on the eye again if you hid it).
- Click away from the sphere to deselect it.
- On the left-hand side, click on the “Loop Cut” tool ![image](https://user-images.githubusercontent.com/106686527/180088808-0930613c-e8b5-407a-b5d8-5110d6de00cf.png) and create cuts that are along the edge of your cut sphere by clicking when the yellow line is horizontal and in the relative area where you want the cut to be. If you need to move the cuts, just click and hold, then drag the cut to where you want it to be. In my case, I didn’t need to do this step since the inner sphere already had lines that aligned with my cut sphere quite nicely.
- Next to the drop down menu in the upper left there will be three cubes. Click on the right most cube (the one with an entire face in white), so that you are only selecting the faces of the sphere.
- Now, highlight the faces that are above and below the cuts that you have made respectively.
![Screen Shot 2022-07-20 at 11 14 18 AM](https://user-images.githubusercontent.com/106686527/180090521-9d877703-bc25-4771-a3cd-3adfca43ec4d.png)
- Delete these faces by pressing X, then clicking delete “Faces.”
- If you rotate your view, you may notice that there are faces on the other side that weren’t deleted. Delete these faces individually.
![Screen Shot 2022-07-20 at 11 14 04 AM](https://user-images.githubusercontent.com/106686527/180092026-3840cb64-9dc6-42d9-8e42-4e6392994f32.png)
- If you switch your viewport shading to “Solid” (in the upper right corner, the second to leftmost sphere that is completely white), you will see something like this.
![Screen Shot 2022-07-20 at 11 18 14 AM](https://user-images.githubusercontent.com/106686527/180090676-9c6569b2-b282-44e1-81bd-8a13f8ee89d5.png)
## Join the Two Surfaces and Fill in the Gap
- Select both surfaces by holding down the shift key, and then press Ctrl+J so that they are now considered one object.
![Screen Shot 2022-07-20 at 11 20 07 AM](https://user-images.githubusercontent.com/106686527/180090934-b668fd32-d032-4969-9081-53b5fb4acf33.png)
- Now, go back into edit mode while still selecting the object (click on the drop down menu in the upper left that right now says “Object Mode”).
- Next to the drop down menu in the upper left there will be three cubes. Click on the middle cube ![image](https://user-images.githubusercontent.com/106686527/180091035-048af7ce-3a26-470e-a623-db0656298d49.png), so that you are only selecting the vertices of the object.
- Select the outermost edges on both surfaces by holding down the Shift key.
![Screen Shot 2022-07-20 at 11 23 44 AM](https://user-images.githubusercontent.com/106686527/180091005-3f98f7d2-5b2f-4508-9700-6bdd03c12ff6.png)
- Press Alt-F to fill in the gap between the two surfaces.
![Screen Shot 2022-07-20 at 11 24 35 AM](https://user-images.githubusercontent.com/106686527/180091076-26d5574e-bab3-43f4-868b-c836ce7ef61a.png)
## Set Material
- Now that we have the general structure of the cornea, we can set the material to match the cornea.
- Click on the red sphere near the bottom![image](https://user-images.githubusercontent.com/106686527/180091233-7e64ef2c-2bc4-4791-8086-cac1bd329041.png) (“Material Properties”) and click “New.”
- In the “Surface” section under “Surface,” click on what may by default say “Principled BSDF” and change it to “Refraction BSDF.”
- Set the “Roughness” to 0.
- Set the IOR (index of refraction) to 1.376 to match that of the cornea.
- You won’t see anything different now, but change your viewing (the spheres in the upper right) to “Viewport Shading” ![image](https://user-images.githubusercontent.com/106686527/180091371-6858a23d-e56b-4c19-bc7e-d22d45c0386d.png).
## There you have it! The cornea lens built in Blender.
![Screen Shot 2022-07-20 at 11 51 40 AM](https://user-images.githubusercontent.com/106686527/180091416-261a7451-c4f8-43f4-bdf7-3093a6ddc682.png)
