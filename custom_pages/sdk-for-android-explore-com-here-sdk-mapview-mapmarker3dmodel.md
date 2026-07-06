---
title: "MapMarker3DModel (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapMarker3DModel →
com.here.NativeBase → com.here.sdk.mapview.MapMarker3DModel

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapMarker3DModel</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a 3D model that can be used by a MapMarker3D to be shown on
the map. Geometry of 3D marker can be provided in form of a Wavefront
OBJ file as specified in http://www.martinreddy.net/gfx/3d/OBJ.spec or
as mesh built via MeshBuilder . For OBJ files, HERE SDK only supports
the following set of features of the OBJ specification: Triangle Meshes
Following vertex attributes must be present: Vertex Position Vertex
Normal Texture Coordinates Geometry must be indexed (contain an Index
Buffer) Face element HERE SDK does not support: Multi Texturing
Materials (mtllib \[external .mtl file name\] ) Lines Higher Order
Surfaces Vendor specific extensions For supported texture formats, HERE
SDK allows the following formats to be specified: JPG, PNG, GPU
compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX. A 3D
mesh can be specified programatically using MeshBuilder and passed to
MapMarker3DModel constructor. This method supports creating a mesh from
quads and triangles. Textured geometry is also supported, the mesh faces
need to have texture coordinates and a texture file needs to be passed
along with the mesh to MapMarker3DModel constructor.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapMarker3DModel.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the reason for a failure to create MapMarker3DModel .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMarker3DModel.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create MapMarker3DModel .

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
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

      MapMarker3DModel(Mesh mesh)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new 3D model from a mesh.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarker3DModel(Mesh mesh,
       String textureFilePath)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new 3D model from mesh and texture.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapMarker3DModel(Mesh mesh,
       String textureFilePath,
       Color color)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new 3D model from mesh, texture and color.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarker3DModel(String geometryFilePath)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new 3D model from path to .obj file.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapMarker3DModel(String geometryFilePath,
       String textureFilePath)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new 3D model from path to .obj file and texture.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarker3DModel(String geometryFilePath,
       String textureFilePath,
       Color color)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new 3D model from path to .obj file, texture and color.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>(java.lang.String,java.lang.String,com.here.sdk.core.Color)"
    class="section detail">

    ### MapMarker3DModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> geometryFilePath,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> textureFilePath,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color)</span>

    </div>

    <div class="block">

    Creates a new 3D model from path to .obj file, texture and color.

    </div>

    Parameters:  
    `geometryFilePath` -

    Absolute path to obj file.

    `textureFilePath` -

    Absolute path to texture file.

    `color` -

    Color to be blend with texture. This color is multiplied with color
    of texture.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.Mesh,java.lang.String,com.here.sdk.core.Color)"
    class="section detail">

    ### MapMarker3DModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><span class="parameters">(@NonNull
    [Mesh](sdk-for-android-explore-com-here-sdk-mapview-mesh "class in com.here.sdk.mapview") mesh,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> textureFilePath,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color)</span>
    throws
    <span class="exceptions">[MapMarker3DModel.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a new 3D model from mesh, texture and color.

    </div>

    Parameters:  
    `mesh` -

    Mesh containing the 3d geometry together with texture coordinates.

    `textureFilePath` -

    Absolute path to texture file.

    `color` -

    Color to be blend with texture. This color is multiplied with color
    of texture.

    Throws:  
    [`MapMarker3DModel.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")

    Indicates what went wrong when the instantiation was attempted.

    </div>
<div id="sdk-for-android-explore-<init>(java.lang.String,java.lang.String)"
    class="section detail">

    ### MapMarker3DModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> geometryFilePath,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> textureFilePath)</span>

    </div>

    <div class="block">

    Creates a new 3D model from path to .obj file and texture.

    </div>

    Parameters:  
    `geometryFilePath` -

    Absolute path to obj file.

    `textureFilePath` -

    Absolute path to texture file.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.Mesh,java.lang.String)"
    class="section detail">

    ### MapMarker3DModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><span class="parameters">(@NonNull
    [Mesh](sdk-for-android-explore-com-here-sdk-mapview-mesh "class in com.here.sdk.mapview") mesh,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> textureFilePath)</span>
    throws
    <span class="exceptions">[MapMarker3DModel.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a new 3D model from mesh and texture.

    </div>

    Parameters:  
    `mesh` -

    Mesh containing the 3d geometry together with texture coordinates.

    `textureFilePath` -

    Absolute path to texture file.

    Throws:  
    [`MapMarker3DModel.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")

    Indicates what went wrong when the instantiation was attempted.

    </div>
<div id="sdk-for-android-explore-<init>(java.lang.String)"
    class="section detail">

    ### MapMarker3DModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> geometryFilePath)</span>

    </div>

    <div class="block">

    Creates a new 3D model from path to .obj file.

    </div>

    Parameters:  
    `geometryFilePath` -

    Absolute path to obj file.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.Mesh)"
    class="section detail">

    ### MapMarker3DModel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3DModel</span><span class="parameters">(@NonNull
    [Mesh](sdk-for-android-explore-com-here-sdk-mapview-mesh "class in com.here.sdk.mapview") mesh)</span>

    </div>

    <div class="block">

    Creates a new 3D model from a mesh.

    </div>

    Parameters:  
    `mesh` -

    Mesh containing the 3d geometry 3D data.

    </div>

  </div>

</div>

