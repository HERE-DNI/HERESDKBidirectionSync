---
title: "MapMarker3DModel (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker3dmodel"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarker3DModel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapMarker3DModel
------------------------------------------------------------------------
public final class MapMarker3DModel extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents a 3D model that can be used by a [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") to be shown on the map. Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in http://www.martinreddy.net/gfx/3d/OBJ.spec or as mesh built via [`MeshBuilder`](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview").

# 1. Creating `MapMarker3DModel` from OBJ file

For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:

- Triangle Meshes
- Following vertex attributes must be present:
  - Vertex Position
  - Vertex Normal
  - Texture Coordinates
  - Geometry must be indexed (contain an Index Buffer)
  - Face element

HERE SDK does not support:

- Multi Texturing
- Materials (mtllib \[external .mtl file name\] )
  - Lines
  - Higher Order Surfaces
  - Vendor specific extensions

For supported texture formats, HERE SDK allows the following formats to be specified: JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.

# 2. Creating `MapMarker3DModel` programatically

A 3D mesh can be specified programatically using [`MeshBuilder`](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview") and passed to `MapMarker3DModel` constructor. This method supports creating a mesh from quads and triangles. Textured geometry is also supported, the mesh faces need to have texture coordinates and a texture file needs to be passed along with the mesh to `MapMarker3DModel` constructor.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode)

Indicates the reason for a failure to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").

`static final class `

  [MapMarker3DModel.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception)

Thrown when a problem occurs while trying to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").

## Constructor Summary

Constructors

Constructor

  Description

  [MapMarker3DModel](#%3Cinit%3E(com.here.sdk.mapview.Mesh))`(`[`Mesh`](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview")` mesh)`

Creates a new 3D model from a mesh.

[MapMarker3DModel](#%3Cinit%3E(com.here.sdk.mapview.Mesh,java.lang.String))`(`[`Mesh`](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview")` mesh, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` textureFilePath)`

Creates a new 3D model from mesh and texture.

[MapMarker3DModel](#%3Cinit%3E(com.here.sdk.mapview.Mesh,java.lang.String,com.here.sdk.core.Color))`(`[`Mesh`](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview")` mesh, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` textureFilePath, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color)`

Creates a new 3D model from mesh, texture and color.

[MapMarker3DModel](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` geometryFilePath)`

Creates a new 3D model from path to .obj file.

[MapMarker3DModel](#%3Cinit%3E(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` geometryFilePath, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` textureFilePath)`

Creates a new 3D model from path to .obj file and texture.

[MapMarker3DModel](#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.core.Color))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` geometryFilePath, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` textureFilePath, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color)`

Creates a new 3D model from path to .obj file, texture and color.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (java.lang.String,java.lang.String,com.here.sdk.core.Color)" class="section detail">

### MapMarker3DModel

public MapMarker3DModel(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) geometryFilePath, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) textureFilePath, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color)

    Creates a new 3D model from path to .obj file, texture and color.
Parameters:
    `geometryFilePath` -

    Absolute path to obj file.

    `textureFilePath` -

    Absolute path to texture file.

    `color` -

    Color to be blend with texture. This color is multiplied with color of texture.
- (com.here.sdk.mapview.Mesh,java.lang.String,com.here.sdk.core.Color)" class="section detail">

### MapMarker3DModel

public MapMarker3DModel(@NonNull [Mesh](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview") mesh, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) textureFilePath, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color) throws [MapMarker3DModel.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")

    Creates a new 3D model from mesh, texture and color.
Parameters:
    `mesh` -

    Mesh containing the 3d geometry together with texture coordinates.

    `textureFilePath` -

    Absolute path to texture file.

    `color` -

    Color to be blend with texture. This color is multiplied with color of texture.

    Throws:
    [`MapMarker3DModel.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview") -

    Indicates what went wrong when the instantiation was attempted.
- (java.lang.String,java.lang.String)" class="section detail">

### MapMarker3DModel

public MapMarker3DModel(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) geometryFilePath, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) textureFilePath)

    Creates a new 3D model from path to .obj file and texture.
Parameters:
    `geometryFilePath` -

    Absolute path to obj file.

    `textureFilePath` -

    Absolute path to texture file.
- (com.here.sdk.mapview.Mesh,java.lang.String)" class="section detail">

### MapMarker3DModel

public MapMarker3DModel(@NonNull [Mesh](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview") mesh, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) textureFilePath) throws [MapMarker3DModel.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")

    Creates a new 3D model from mesh and texture.
Parameters:
    `mesh` -

    Mesh containing the 3d geometry together with texture coordinates.

    `textureFilePath` -

    Absolute path to texture file.

    Throws:
    [`MapMarker3DModel.InstantiationException`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview") -

    Indicates what went wrong when the instantiation was attempted.
- (java.lang.String)" class="section detail">

### MapMarker3DModel

public MapMarker3DModel(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) geometryFilePath)

    Creates a new 3D model from path to .obj file.
Parameters:
    `geometryFilePath` -

    Absolute path to obj file.
- (com.here.sdk.mapview.Mesh)" class="section detail">

### MapMarker3DModel

public MapMarker3DModel(@NonNull [Mesh](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview") mesh)

    Creates a new 3D model from a mesh.
Parameters:
    `mesh` -

    Mesh containing the 3d geometry 3D data.
