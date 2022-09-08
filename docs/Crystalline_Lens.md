# Building The Lens
![Screen Shot 2022-06-22 at 12 56 42 PM](https://user-images.githubusercontent.com/106686527/176088615-0c8f2c3c-66f3-4a52-84bb-b553647ebfdf.png)![Screen Shot 2022-06-27 at 9 53 49 PM](https://user-images.githubusercontent.com/106686527/176088650-591f9742-ad95-4cdc-abf8-75ac0063fe03.png)![Screen Shot 2022-06-27 at 9 53 54 PM](https://user-images.githubusercontent.com/106686527/176088676-3be5a2a1-93a6-451f-8f96-bebc713fd5f3.png)



## Download Blender
![image](https://user-images.githubusercontent.com/106686527/175160863-447fe426-adad-4917-9e5c-40c116f97815.png)
https://www.blender.org
- Blender is a free, open-source software where you can build 3D models, shade them, and even later animate your creation! Because of how powerful it is and its many different types of lights, we will be using Blender in our project. Plus, it has a monkey! To download Blender, click on the link above and follow the website's instructions. If you want a general guide to how to use Blender, they also have a YouTube playlist where they walk you through the fundamentals on how to use their software. Simply search "Blender fundamentals" into Youtube. The playlist should be the first result, below the ad of course. 

## Draw 2 Spheres

- Delete the default cube by clicking on it (if it is not already highlighted in orange), pressing X on your keyboard, and clicking "Delete" on the pop-up.
- In the upper left, click on “Add” -> “Mesh” -> “UV Sphere”

![Screen Shot 2022-06-26 at 9 15 06 PM](https://user-images.githubusercontent.com/106686527/175853356-c4f0c47f-7a15-4c3f-a707-64780ea89340.png)

- Right click on the sphere and select “Shade Smooth.” This will take away the geometric planes of the UV sphere and will give you something that looks more like a ball.

![image](https://user-images.githubusercontent.com/106686527/175162483-df87b2a9-f054-40c7-a0fd-f87084594043.png)

- Press Ctrl+C, then Ctrl+V to get an identical sphere in the same spot The only difference you will likely see is that the sphere is highlighted in a darker orange. This is fine! Both spheres are present, but just in the same location, making it look like one sphere. If you really want to make sure though, in the upper right corner, you'll see a list of all the objects in your scene such as the light, camera, and, hopefully!, two spheres.

![Screen Shot 2022-06-26 at 9 17 21 PM](https://user-images.githubusercontent.com/106686527/175853560-29d1bbd8-fec2-4c19-b177-d5dd8cfe9723.png)


## Overlap The Spheres
- In the upper right of your viewport, there is a three pronged stick labelled with X-Y-Z. This controls the orientation of your view. For now, click on the Y ball.
![image](https://user-images.githubusercontent.com/106686527/175853891-00c2d4ac-9407-4524-b361-db950ea24bc8.png)

- Go to the list in the upper right corner and select one of the spheres (it doesn’t matter which one). 
- Then, go to the properties editor (on the right just underneath the list of your objects) and click on the orange square that has lines around its corners: the object properties tab. ![image](https://user-images.githubusercontent.com/106686527/175853933-746fc25a-ec89-4186-9017-9a043324077c.png)

- In the “Transform” drop down menu, set the “Z” location to be 0.4.
- Repeat the last three steps for the second sphere, but now set the “Z” location to be -0.6.
- You should have something like this.

![Screen Shot 2022-06-20 at 9 34 11 PM](https://user-images.githubusercontent.com/106686527/175164749-62b10042-9a94-4807-9309-662d8db273a1.png)

## Shape the 2 Spheres
- Now, below the “Location” section in the “Transform” tab, there will be the “Scale” section. The human eye lens is not symmetrical as you can see. 

![Schematic_diagram_of_the_human_eye_en svg](https://user-images.githubusercontent.com/106686527/175165358-9f389b1e-87d2-4de7-bc86-a4e01f908c11.png)
(https://en.wikipedia.org/wiki/Lens_%28anatomy%29) 
- To get a similar effect in Blender, increase the “Z” component of the sphere (using scale) for the top sphere and decrease the “X” and “Y” component. The X and Y component should be scaled to the same amount to keep a circular shape. This will lengthen the sphere vertically and make it “pointier” at the bottom.
- For the bottom sphere, increase the “X” and “Y” and decrease the “Z” for a flatter top. 
- The last two steps may seem counterintuitive, but the top sphere creates the bottom part of the lens, and the bottom sphere creates the top part of the lens since we are taking the two intersections of the spheres. If this doesn't make sense quite yet, it might once we form the lens.
- Don’t worry about accuracy when scaling as the human lens stretches and shrinks as the eye focuses on something close or far away through a process called accommodation. This means that there are no set measurements of the lens, so our only goal for now will be to get the general shape.

![Screen Shot 2022-06-20 at 9 44 27 PM](https://user-images.githubusercontent.com/106686527/175166041-796a1568-e73a-4b31-aacf-a0312afe3156.png)

## Take Sphere Intersections
- Click the blue wrench, right underneath the properties editor![image](https://user-images.githubusercontent.com/106686527/175854508-084ad21b-4c5b-4ab9-9cf8-d9b830823fc2.png): the “Properties Modifier.”
- Have either of the spheres selected and press “Add Modifier” -> “Boolean” (under "Generate").
- Select “Intersect.” 
- In the “Object” section, select the eyedropper-looking tool, and press the upper sphere.
- The sphere you didn’t click on with the eyedropper tool will look like it was deleted. What happened is that only the part of the sphere that "intersects" the other sphere was kept. The other part was whisked away!
- Click on the down arrow next to the camera in the very top of the “Boolean” tab and press “apply.” ![image](https://user-images.githubusercontent.com/106686527/175854998-118a89d5-bb45-4072-8928-3a41deb70b8f.png) 
- If you skip this step, the shape from the last step will be deleted, and you will just be left with the remaining sphere.
- Select the sphere that is still intact and delete it.
![Screen Shot 2022-06-20 at 9 52 55 PM](https://user-images.githubusercontent.com/106686527/176087179-7c1f9ec9-2be5-4e38-86ef-3f7e5f2b71b2.png)
- Go to the properties editor and click on the object properties![image](https://user-images.githubusercontent.com/106686527/175853933-746fc25a-ec89-4186-9017-9a043324077c.png).
- Set the Y rotation to be 90 degrees, set the X location to -0.4 for orientation purposes.



## Set Material to be Transparent

![Screen Shot 2022-06-22 at 1 49 48 PM](https://user-images.githubusercontent.com/106686527/175166856-dda844b3-f152-413b-b2ec-9a656bab3c02.png)

- Click on the red sphere near the bottom ![image](https://user-images.githubusercontent.com/106686527/175855327-34a036c3-39e9-47b0-a39d-69afa1525591.png)
 (“Material Properties”) and click “New.”
- In the “Surface” section under “Surface,” click on what may by default say “Principled BSDF” and change it to “Refraction BSDF.”
- Set the “Roughness” to 0.
- Set the IOR (index of refraction) to 1.386 to match that of the human lens.
- You won’t see anything different now, but change your viewing (the spheres in the upper right) to “Viewport Shading” (the third sphere from the left).
- Before checking, go back to the Modifier Properties (the blue wrench in the properties editor) and add a “Subdivision Surface” modifier to smooth out any dimples on the edge of the lens.
- What is happening is that Blender is taking the environment from one of their other workspaces ("Shading") and placing the lens in that environment while keeping you in the current one ("Layout") to give the impression of transparency. To see for yourself, go up to the tippy-top where you will see a list of Blender's workspaces like "Layout" (your current one), "Modeling," "Sculpting," and (what you will want to click on) "Shading."
![image](https://user-images.githubusercontent.com/106686527/175856013-f51eb4c0-f37d-468d-831e-45ddc951d6e2.png)

## Add Suture Lines

### What Are Suture Lines?
![B9780323036566500160_f11-07-9780323036566](https://user-images.githubusercontent.com/106686527/175158656-81abdab4-ea4d-401e-aa37-2cc60d882b69.jpg)
https://entokey.com/the-lens/

Suture lines are transparent, ribbon like structures that are part of the human lens that can explain the reason we see point lights as, well, pointy. They affect the light coming into the eye through a process called diffraction. They are made out of lens fibers and have the general shape as seen above, with two Y shapes (one on the front and one upside down behind) being the center of where the ribbons spring out from. Suture lines are possibly the whole reason for the star images phenomenon, so the next few steps may be daunting, but are crucial. To read more about suture lines and the structure of the eye in general, click here:
https://www.sciencedirect.com/science/article/pii/S1888429609700184

### Making the Main Anterior (front-facing) Suture Lines
![Screen Shot 2022-06-22 at 2 02 29 PM](https://user-images.githubusercontent.com/106686527/176087273-f77f5bd9-fa62-4c06-a9ef-483233b2b351.png)
- Switch back to the “Viewport Shading” view (second sphere in the top right).
- Switch from “Object Mode” to “Edit Mode” in the top left.![image](https://user-images.githubusercontent.com/106686527/175856133-ef236313-1be6-446d-8448-5dd1ef360b09.png)
- Click away from the object or press Alt+A to deselect the object.
- Orient yourself so that you’re facing the flatter part of the lens (I’ve found that using the X-Y-Z tool in the upper right is helpful; for me, I clicked X to face the flat part of my lens).
- Using the annotation tool, on the left, the pen amongst all the rectangles![image](https://user-images.githubusercontent.com/106686527/175856197-2c427e5b-65de-437e-851a-62f940995c90.png), draw a Y shape centered on the center of the circle. 
- Go up and click “Note” in the upper left corner right next to annotation and whatever color your pen is at the moment.![image](https://user-images.githubusercontent.com/106686527/175856266-73deecff-9247-45ca-ac90-d74137abcd29.png)
- Change the name of the annotation from “Annotation” to “Anterior Suture Lines,” you should be able to do this from the first box.
![Screen Shot 2022-06-24 at 9 24 55 PM](https://user-images.githubusercontent.com/106686527/176087394-be3e2c56-7160-4a14-9d1e-2d935e3d6d03.png)
- Using the knife tool ![image](https://user-images.githubusercontent.com/106686527/175856307-8e265e10-a946-460e-8b03-4a8c438bdcc3.png)
, cut out your Y. I did one cut above each part of the upper half of the Y, and two cuts surrounding the bottom half. 
- I only outlined the sides of the Y because now we will change the material of those sections.
- In the properties editor, click on the bottom most red sphere (“Material Properties”) and click on the plus sign next to your array of already there materials. 
- Then, select the “New” button.
- Name this new material “Suture Lines.”
- As with the lens material, change the surface setting to “Refraction BSDF,” roughness to zero, but now, set the IOR to 1.
- In the upper right corner with the three sets of cubes, select the third one from the left ![image](https://user-images.githubusercontent.com/106686527/176085881-75665f33-46df-489d-b56c-a922ac369cb7.png). This will make it so that you are selecting faces as opposed to vertices or points.
- Holding the shift key, select all of the faces in your Y-shape.
- Then, making sure they are all still selected, click on the “Assign” button just below your materials. This will make it so that the faces you just selected are now in this material. 
- If you want to double-check that the Suture Line material was assigned, you can click on “Select” which will select all surfaces with that material.
- In the viewport shading, you will see something like this.
![Screen Shot 2022-06-22 at 2 17 40 PM](https://user-images.githubusercontent.com/106686527/176087483-afab30b2-dd7a-49c8-8fa1-643632a34576.png)

### Making the Main Posterior (back-facing) Suture Lines
- Go to the other side of the lens (the more curved part). You can do this by clicking on the X ball again on the X-Y-Z tool in the upper right.
- We will want to make another annotation for the other side’s suture lens, so click on the annotation tool again, go back to “Note,” and click on the two pieces of paper in the pop-up to create a new annotation. Name this one “Posterior Suture Lines,” and select a new color from the other annotation. I went with a pink!
- You will want to draw another Y, but this time it will be upside down.
![Screen Shot 2022-06-22 at 2 29 22 PM](https://user-images.githubusercontent.com/106686527/176087756-282f9ced-18ef-4634-a6fc-069127680443.png)
- Use the knife tool again, and cut out sections of your upside down Y, and change those sections to your Suture Lines material.
![Screen Shot 2022-06-22 at 2 38 02 PM](https://user-images.githubusercontent.com/106686527/176087818-7b97bccb-fac4-461f-9d72-8308a5de3b1c.png)

### Connecting Your Suture Lines
- Suture lines wrap around and connect on both sides of the lens, so we will want ours to do the same.
- Going back to our suture lines material in the material properties section ![image](https://user-images.githubusercontent.com/106686527/176086253-bf290b34-01dd-4026-bf4e-f022bfe21719.png), click “Select.” If you are oriented correctly (facing one side of the lens so that it looks like a circle), you will see faint orange sections peeking out from the other side.
 ![Screen Shot 2022-06-22 at 2 43 00 PM](https://user-images.githubusercontent.com/106686527/175756475-ceb18a79-8ade-42d3-9c3d-27d4ed74e481.png)
 - Using the annotation tool again![image](https://user-images.githubusercontent.com/106686527/176086308-fc5b3e82-c961-4073-ba38-97c2fafdb214.png)
, draw lines originating from the orange sections, and connect them to the already present suture lines on that side.
 - Then, use your knife tool ![image](https://user-images.githubusercontent.com/106686527/176086357-7fab981f-0260-4b90-8a6e-dadbda598898.png) and along your drawing, cut out your suture lines.
![Screen Shot 2022-06-22 at 2 45 55 PM](https://user-images.githubusercontent.com/106686527/176087963-57a4c933-e5b8-459b-895f-9195a5b9e6b9.png)
 - Select the faces of your newly cut suture lines, and assign them to the Suture Lines material
- There you have it! Your first suture lines! I do suggest marking every line you make and filling it in as it can become difficult to distinguish a suture line from a line that defines the geometry of the sphere.

### Making the Rest of the Suture Lines
![Screen Shot 2022-06-22 at 12 57 04 PM](https://user-images.githubusercontent.com/106686527/176086648-cdc0b5bd-c3e8-49b4-801e-ea151065b8bd.png)![Screen Shot 2022-06-22 at 12 56 59 PM](https://user-images.githubusercontent.com/106686527/176086699-2819609c-e374-4555-9aab-c06d8e6a1f74.png)
- Now, using the annotation tool, stay on one side of the lens, and draw more suture lines branching off from your Y. It doesn’t have to be symmetrical as these patterns are unique to each human. 
- Again, use the knife tool![image](https://user-images.githubusercontent.com/106686527/176086357-7fab981f-0260-4b90-8a6e-dadbda598898.png) to cut out sections following your drawn suture lines.
- Once you’re done, you should have something like this. It doesn't matter which side you initially draw your lines on, but here I am showing the front side of the lens.

![Screen Shot 2022-06-18 at 8 56 53 PM](https://user-images.githubusercontent.com/106686527/176086895-1dfb534e-4098-4c84-84b9-537ed4de94d6.png)
- Select the faces of your suture lines and then change the material from “Lens” to “Suture Lines.”
- Then, switch to the other side of the lens, go back to our suture lines material in the material properties section ![image](https://user-images.githubusercontent.com/106686527/176086508-d09242c8-14ee-431c-b668-d7f495cc9cc9.png), click “Select.” You should see orange marks on the edge of your lens from the suture lines you drew on the other side. If you don’t see them, then your cuts likely didn’t make it all the way to the edge of the lens. Simply go back to the other side of the lens, and make sure the cut makes it completely through the last section of the lens. 
- Connect the orange marks to the Y on the other side of the lens with the annotation tool, cut the lines out with the knife tool, and then switch the material to Suture Lines in the Material Properties Editor. 
- You should have something like this if you switch to Viewport Shading.
![Screen Shot 2022-06-22 at 12 56 42 PM](https://user-images.githubusercontent.com/106686527/175756804-5c3dcfec-4aca-4f79-af52-317b15ff4f79.png)
- There you have it! The human lens built in Blender.

