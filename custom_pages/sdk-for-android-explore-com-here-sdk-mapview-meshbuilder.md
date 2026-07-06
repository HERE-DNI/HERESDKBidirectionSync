---
title: "MeshBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-meshbuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MeshBuilder →
com.here.NativeBase → com.here.sdk.mapview.MeshBuilder

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Direct Known Subclasses:  
[`QuadMeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-quadmeshbuilder "class in com.here.sdk.mapview"),
[`TriangleMeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public class
</span><span class="element-name type-name-label">MeshBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Builder for meshes. Such meshes can contain different kinds of
primitives, like quads or triangles. Both primitives support adding
texture coordinates that are mapped to the corners of the primitives.
See TriangleMeshBuilder and QuadMeshBuilder for more details. Note:
Normals cannot be set as they are not necessary when using the
MeshBuilder . Example how to build a cube using QuadMeshBuilder Mesh
cube = new MeshBuilder() .quad(new Point3D(0.5, 0.5, 0.5), new
Point3D(-0.5, 0.5, 0.5), new Point3D(0.5, -0.5, 0.5), new Point3D(-0.5,
-0.5, 0.5)) .quad(new Point3D(-0.5, 0.5, -0.5), new Point3D(0.5, 0.5,
-0.5), new Point3D(-0.5, -0.5, -0.5), new Point3D(0.5, -0.5, -0.5))
.quad(new Point3D(0.5, 0.5, -0.5), new Point3D(0.5, 0.5, 0.5), new
Point3D(0.5, -0.5, -0.5), new Point3D(0.5, -0.5, 0.5)) .quad(new
Point3D(-0.5, 0.5, 0.5), new Point3D(-0.5, 0.5, -0.5), new Point3D(-0.5,
-0.5, 0.5), new Point3D(-0.5, -0.5, -0.5)) .quad(new Point3D(-0.5, 0.5,
0.5), new Point3D(0.5, 0.5, 0.5), new Point3D(-0.5, 0.5, -0.5), new
Point3D(0.5, 0.5, -0.5)) .quad(new Point3D(0.5, -0.5, 0.5), new
Point3D(-0.5, -0.5, 0.5), new Point3D(0.5, -0.5, -0.5), new
Point3D(-0.5, -0.5, -0.5)) .build();

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      MeshBuilder()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an instance of MeshBuilder.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
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

  [`Mesh`](sdk-for-android-explore-com-here-sdk-mapview-mesh "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      build()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`QuadMeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-quadmeshbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      quad(Point3D a,
       Point3D b,
       Point3D c,
       Point3D d)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a quad.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TriangleMeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      triangle(Point3D a,
       Point3D b,
       Point3D c)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a triangle.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### MeshBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MeshBuilder</span>()

    </div>

    <div class="block">

    Constructs an instance of MeshBuilder.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"
    class="section detail">

    ### triangle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TriangleMeshBuilder](sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">triangle</span><span class="parameters">(@NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") a,
    @NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") b,
    @NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") c)</span>

    </div>

    <div class="block">

    Adds a triangle. Triangle visibility is determined via back-face
    culling. Front-facing triangles are expected to have
    counter-clockwise winding.

    </div>

    Parameters:  
    `a` -

    First vertex of the triangle.

    `b` -

    Second vertex of the triangle.

    `c` -

    Third vertex of the triangle.

    Returns:  
    A
    [`TriangleMeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-trianglemeshbuilder "class in com.here.sdk.mapview")
    instance.

    </div>

  - <div id="sdk-for-android-explore-quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D)"
    class="section detail">

    ### quad

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[QuadMeshBuilder](sdk-for-android-explore-com-here-sdk-mapview-quadmeshbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">quad</span><span class="parameters">(@NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") a,
    @NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") b,
    @NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") c,
    @NonNull
    [Point3D](sdk-for-android-explore-com-here-sdk-core-point3d "class in com.here.sdk.core") d)</span>

    </div>

    <div class="block">

    Adds a quad. Internally, this will be transformed into triangles abc
    and bdc. Triangle visibility is determined via back-face culling.
    Front-facing triangles are expected to have counter-clockwise
    winding.

    </div>

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
    A
    [`QuadMeshBuilder`](sdk-for-android-explore-com-here-sdk-mapview-quadmeshbuilder "class in com.here.sdk.mapview")
    instance.

    </div>

  - <div id="sdk-for-android-explore-build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Mesh](sdk-for-android-explore-com-here-sdk-mapview-mesh "class in com.here.sdk.mapview")</span> <span class="element-name">build</span>()

    </div>

    Returns:  
    mesh containing added geometry or 'null' if no geometry was added.

    </div>

  </div>

</div>

