# Human-Lens

Welcome to this repo!

## Rendering the Blender Animations

To render a blender animation, `cd ` into the `src` directory and run the following (for machine with CUDA support):

```
blender -b file.blend -a -- --cycles-device CUDA
```

output files will be saved in `/tmp`. If you would like to save the output files somewhere else run:

```
blender -b file.blend -o path/to/output/frame_##### -a -- --cycles-device CUDA
```
which saves the files to `path/to/output/` with names like `frame_00001,frame_00002,...`
