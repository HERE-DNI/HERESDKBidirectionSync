---
title: "TriangleMeshBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MeshBuildercom.here.sdk.mapview.TriangleMeshBuilder
→ com.here.NativeBase →
com.here.sdk.mapview.MeshBuildercom.here.sdk.mapview.TriangleMeshBuilder
→ com.here.sdk.mapview.MeshBuilder →
com.here.sdk.mapview.TriangleMeshBuilder

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TriangleMeshBuilder</span>
<span class="extends-implements">extends
[MeshBuilder](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder "class in com.here.sdk.mapview")</span>

</div>

<div class="block">

Builder for a single triangle.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withTextureCoordinates(Anchor2D a,
       Anchor2D b,
       Anchor2D c)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds texture coordinates to a triangle.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class com.here.sdk.mapview.[MeshBuilder](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder "class in com.here.sdk.mapview")

  [`build`](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#build()), [`quad`](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)), [`triangle`](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-withTextureCoordinates(com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D,com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### withTextureCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MeshBuilder](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withTextureCoordinates</span><span class="parameters">(@NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") a,
    @NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") b,
    @NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") c)</span>

    </div>

    <div class="block">

    Adds texture coordinates to a triangle. Coordinates are specified as
    with \<0,0\> representing the bottom-left and \<1,1\> upper-right
    corner.

    </div>

    Parameters:  
    `a` -

    Texture coordinate for vertex a. See
    [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    `b` -

    Texture coordinate for vertex b. See
    [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    `c` -

    Texture coordinate for vertex c. See
    [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.triangle(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    Returns:  
    A
    [`MeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder "class in com.here.sdk.mapview")
    instance.

    </div>

  </div>

</div>

