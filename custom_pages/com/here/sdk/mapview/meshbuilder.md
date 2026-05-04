---
title: "MeshBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmeshbuilder"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MeshBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MeshBuilder
Direct Known Subclasses:
[`QuadMeshBuilder`](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview"), [`TriangleMeshBuilder`](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public class MeshBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder for meshes. Such meshes can contain different kinds of primitives, like quads or triangles. Both primitives support adding texture coordinates that are mapped to the corners of the primitives. See [`TriangleMeshBuilder`](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview") and [`QuadMeshBuilder`](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview") for more details.

Note: Normals cannot be set as they are not necessary when using the [`MeshBuilder`](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview").

**Example how to build a cube using [`QuadMeshBuilder`](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview")**

        Mesh cube = new MeshBuilder()
             .quad(new Point3D(0.5, 0.5, 0.5),
                 new Point3D(-0.5, 0.5, 0.5),
                 new Point3D(0.5, -0.5, 0.5),
                 new Point3D(-0.5, -0.5, 0.5))
             .quad(new Point3D(-0.5, 0.5, -0.5),
                 new Point3D(0.5, 0.5, -0.5),
                 new Point3D(-0.5, -0.5, -0.5),
                 new Point3D(0.5, -0.5, -0.5))
             .quad(new Point3D(0.5, 0.5, -0.5),
                 new Point3D(0.5, 0.5, 0.5),
                 new Point3D(0.5, -0.5, -0.5),
                 new Point3D(0.5, -0.5, 0.5))
             .quad(new Point3D(-0.5, 0.5, 0.5),
                 new Point3D(-0.5, 0.5, -0.5),
                 new Point3D(-0.5, -0.5, 0.5),
                 new Point3D(-0.5, -0.5, -0.5))
             .quad(new Point3D(-0.5, 0.5, 0.5),
                 new Point3D(0.5, 0.5, 0.5),
                 new Point3D(-0.5, 0.5, -0.5),
                 new Point3D(0.5, 0.5, -0.5))
             .quad(new Point3D(0.5, -0.5, 0.5),
                 new Point3D(-0.5, -0.5, 0.5),
                 new Point3D(0.5, -0.5, -0.5),
                 new Point3D(-0.5, -0.5, -0.5))
             .build();

## Constructor Summary

Constructors

Constructor

  Description

  [MeshBuilder](#%3Cinit%3E())`()`

Constructs an instance of MeshBuilder.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`Mesh`](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview")

  [build](#build())`()`

  [`QuadMeshBuilder`](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview")

  [quad](#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))`(`[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` a, `[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` b, `[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` c, `[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` d)`

Adds a quad.

[`TriangleMeshBuilder`](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview")

  [triangle](#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))`(`[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` a, `[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` b, `[`Point3D`](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")` c)`

Adds a triangle.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### MeshBuilder

public MeshBuilder()

    Constructs an instance of MeshBuilder.

## Method Details

### triangle

@NonNull public [TriangleMeshBuilder](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview") triangle(@NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") a, @NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") b, @NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") c)

    Adds a triangle.

    Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have counter-clockwise winding.
Parameters:
    `a` -

    First vertex of the triangle.

    `b` -

    Second vertex of the triangle.

    `c` -

    Third vertex of the triangle.

    Returns:
    A [`TriangleMeshBuilder`](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview") instance.

### quad

@NonNull public [QuadMeshBuilder](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview") quad(@NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") a, @NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") b, @NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") c, @NonNull [Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core") d)

    Adds a quad. Internally, this will be transformed into triangles abc and bdc.

    Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have counter-clockwise winding.
Parameters:
    `a` -

    First vertex of quad.

    `b` -

    Second vertex of the quad.

    `c` -

    Third vertex of the quad.

    `d` -

    Fourth vertex of the quad.

    Returns:
    A [`QuadMeshBuilder`](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview") instance.

### build

@Nullable public [Mesh](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview") build()
Returns:
    mesh containing added geometry or 'null' if no geometry was added.
