# Building The Lens
![Screen Shot 2022-06-22 at 12 56 42 PM](https://user-images.githubusercontent.com/106686527/175144999-d0cf6eb0-7a57-41b9-9ccb-71f8502b7a10.png)


## Download Blender
![image](https://user-images.githubusercontent.com/106686527/175160863-447fe426-adad-4917-9e5c-40c116f97815.png)
https://www.blender.org

## Draw 2 Spheres

- Delete the default cube
- In the upper left, click on “Add” -> “Mesh” -> “UV Sphere”

![Screen Shot 2022-06-22 at 4 10 39 PM](https://user-images.githubusercontent.com/106686527/175163120-eba58310-12ab-4fdf-a5f0-04c56a80587c.png)

- Right click on the sphere and select “Shade Smooth.” This will take away the geometric planes of the UV sphere and will give you something that looks more like a ball.

![image](https://user-images.githubusercontent.com/106686527/175162483-df87b2a9-f054-40c7-a0fd-f87084594043.png)

- Press Ctrl+C, then Ctrl+V to get an identical sphere in the same spot The only difference you will likely see is that the sphere is highlighted in a darker orange. This is fine! Both spheres are present, but just in the same location, making it look like one sphere. If you really want to make sure though, in the upper right corner, you'll see a list of all the objects in your scene such as the light, camera, and, hopefully!, two spheres.

## Overlap The Spheres
- In the upper right of your viewport, there is a three pronged stick labelled with X-Y-Z. This controls the orientation of your view. For now, click on the Y ball.
- Go to the list in the upper right corner and select one of the spheres (it doesn’t matter which one). 
- Then, go to the properties editor just below and click on the orange square that has lines around its corners: the object properties tab. 
- In the “Transform” drop down menu, set the “Z” location to be 0.4.
- Repeat the last three steps for the second sphere, but now set the “Z” location to be -0.6.
- You should have something like this.

![Screen Shot 2022-06-20 at 9 34 11 PM](https://user-images.githubusercontent.com/106686527/175164749-62b10042-9a94-4807-9309-662d8db273a1.png)

## Shape the 2 Spheres
- Now, below the “Location” section in the “Transform” tab, there will be the “Scale” section. The human eye lens is not symmetrical as you can see. 
![Schematic_diagram_of_the_human_eye_en svg](https://user-images.githubusercontent.com/106686527/175165358-9f389b1e-87d2-4de7-bc86-a4e01f908c11.png)
(https://user-images.githubusercontent.com/106686527/175165097-a80794ce-79f5-4458-849d-52cfb9566a24.png)](https://en.wikipedia.org/wiki/Lens_%28anatomy%29) https://en.wikipedia.org/wiki/Lens_%28anatomy%29
- To get a similar effect in Blender, increase the “Z” component of the sphere (using scale) for the top sphere and decrease the “X” and “Y” component. The X and Y component should be scaled to the same amount to keep a circular shape. This will lengthen the sphere vertically and make it “pointier” at the bottom.
- For the bottom sphere, increase the “X” and “Y” and decrease the “Z” for a flatter top. This may seem counterintuitive, but the top sphere creates the bottom part of the lens, and the bottom sphere creates the top part of the lens.
- Don’t worry about accuracy when scaling as the human lens stretches and shrinks through a process called accommodation.

![Screen Shot 2022-06-20 at 9 44 27 PM](https://user-images.githubusercontent.com/106686527/175166041-796a1568-e73a-4b31-aacf-a0312afe3156.png)

## Take Sphere Intersections
- Click the blue wrench, right underneath the properties editor, which is the “Properties Modifier.”
- Have either of the spheres selected and press “Add Modifier” -> “Boolean.”
- Select “Intersect.”
- In the “Object” section, select the eyedropper-looking tool, and press the upper sphere.
- The sphere you didn’t click on will look like it was deleted.
- Click on the down arrow next to the camera in the very top of the “Boolean” tab and press “apply.”
- Select the sphere that is still intact and delete it.
- You will see something like this.
- Go to the properties editor and click on the object properties.
- Set the Y rotation to be 90 degrees, set the X location to -0.4, and you will see the following image.

![Screen Shot 2022-06-20 at 9 52 55 PM](https://user-images.githubusercontent.com/106686527/175156178-b4749b7a-b4b4-44e2-911b-0fb27fd35274.png)


## Set Material to be Transparent

![Screen Shot 2022-06-22 at 1 49 48 PM](https://user-images.githubusercontent.com/106686527/175166856-dda844b3-f152-413b-b2ec-9a656bab3c02.png)

- Click on the red sphere near the bottom (“Material Properties”) and click “New.”
- In the “Surface” section under “Surface,” click on what may by default say “Principled BSDF” and change it to “Refraction BSDF.”
- Set the “Roughness” to 0.
- Set the IOR (index of refraction) to 1.386 to match that of the human lens.
- You won’t see anything different now, but change your viewing (the spheres in the upper right) to “Viewport Shading” (the third sphere from the left).
- Before checking, go back to the Modifier Properties (the blue wrench in the properties editor) and add a “Subdivision Surface” modifier to smooth out any dimples on the edge of the lens.



## Add Suture Lines

### What Are Suture Lines?
![B9780323036566500160_f11-07-9780323036566](https://user-images.githubusercontent.com/106686527/175158656-81abdab4-ea4d-401e-aa37-2cc60d882b69.jpg)
https://entokey.com/the-lens/

### Sketch Suture Lines on Lens
![Screen Shot 2022-06-22 at 2 29 22 PM](https://user-images.githubusercontent.com/106686527/175160297-06df03cd-8796-47c0-bc0d-fd4a658910cd.png)
![Screen Shot 2022-06-19 at 9 14 13 PM](https://user-images.githubusercontent.com/106686527/175160228-b00aef88-0541-41b6-a8d6-20b3faa0edc8.png)
![Screen Shot 2022-06-22 at 11 56 32 AM](https://user-images.githubusercontent.com/106686527/175160557-c1ba83ec-252f-452b-8ca4-426a1c653c5a.png)



### Cut Suture Lines Out 
![Screen Shot 2022-06-22 at 2 36 24 PM](https://user-images.githubusercontent.com/106686527/175160370-4ff5c63a-0811-4420-817a-0029f8105c49.png)
![Screen Shot 2022-06-22 at 2 43 00 PM](https://user-images.githubusercontent.com/106686527/175160409-33210e8c-42f3-4c17-aeb3-9e68613f72d2.png)
![Screen Shot 2022-06-22 at 2 45 55 PM](https://user-images.githubusercontent.com/106686527/175160429-8e675382-b1cd-4f8c-8914-7f18dbb12ca7.png)
![Screen Shot 2022-06-22 at 2 59 49 PM](https://user-images.githubusercontent.com/106686527/175160434-5769a617-6374-4286-ba30-416fbd0b0692.png)


### Change Material
![Screen Shot 2022-06-22 at 2 59 49 PM](https://user-images.githubusercontent.com/106686527/175160508-9c61fffb-1b67-4b5a-a727-1c8b05db6b26.png)
![Screen Shot 2022-06-22 at 11 56 32 AM](https://user-images.githubusercontent.com/106686527/175160597-ac91e494-911a-4ea2-a3c7-0a2aeb49caab.png)


