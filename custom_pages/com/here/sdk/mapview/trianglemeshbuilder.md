---
title: "TriangleMeshBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrianglemeshbuilder"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TriangleMeshBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
[com.here.sdk.mapview.MeshBuilder](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview")
com.here.sdk.mapview.TriangleMeshBuilder
------------------------------------------------------------------------
public final class TriangleMeshBuilder extends [MeshBuilder](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview")
Builder for a single triangle.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`MeshBuilder`](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview")

  [withTextureCoordinates](#withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` a, `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` b, `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` c)`

Adds texture coordinates to a triangle.

### Methods inherited from class com.here.sdk.mapview.[MeshBuilder](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview")

  [`build`](sdk-for-android-explore-api-reference-latestmeshbuilder#build()), [`quad`](sdk-for-android-explore-api-reference-latestmeshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)), [`triangle`](sdk-for-android-explore-api-reference-latestmeshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### withTextureCoordinates

@NonNull public [MeshBuilder](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview") withTextureCoordinates(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") a, @NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") b, @NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") c)

    Adds texture coordinates to a triangle. Coordinates are specified as `<u,v>` with `<0,0>` representing the bottom-left and `<1,1>` upper-right corner.
Parameters:
    `a` -

    Texture coordinate for vertex a. See [`MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)`](sdk-for-android-explore-api-reference-latestmeshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

    `b` -

    Texture coordinate for vertex b. See [`MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)`](sdk-for-android-explore-api-reference-latestmeshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

    `c` -

    Texture coordinate for vertex c. See [`MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)`](sdk-for-android-explore-api-reference-latestmeshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

    Returns:
    A [`MeshBuilder`](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview") instance.
