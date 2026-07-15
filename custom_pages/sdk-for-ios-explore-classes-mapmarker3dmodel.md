---
title: "MapMarker3DModel Class Reference"
slug: "sdk-for-ios-explore-classes-mapmarker3dmodel"
---

# MapMarker3DModel

<div class="declaration">

<div class="language">

``` highlight
public class MapMarker3DModel
```

``` highlight
extension MapMarker3DModel: NativeBase
```

``` highlight
extension MapMarker3DModel: Hashable
```

</div>

</div>

Represents a 3D model that can be used by a <a href="sdk-for-ios-explore-classes-mapmarker3d">`MapMarker3D`</a> to be shown on the map. Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in <http://www.martinreddy.net/gfx/3d/OBJ.spec> or as mesh built via <a href="sdk-for-ios-explore-classes-meshbuilder">`MeshBuilder`</a>.

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

A 3D mesh can be specified programatically using <a href="sdk-for-ios-explore-classes-meshbuilder">`MeshBuilder`</a> and passed to `MapMarker3DModel` constructor. This method supports creating a mesh from quads and triangles. Textured geometry is also supported, the mesh faces need to have texture coordinates and a texture file needs to be passed along with the mesh to `MapMarker3DModel` constructor.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16MapMarker3DModelC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3dmodel#/s:7heresdk16MapMarker3DModelC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create `MapMarker3DModel`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(geometryFilePath: textureFilePath: color: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D model from path to .obj file, texture and color.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geometryFilePath : String , textureFilePath : String , color : UIColor )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>geometryFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to obj file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textureFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to texture file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>Color to be blend with texture. This color is multiplied with color of texture.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(mesh: textureFilePath: color: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D model from mesh, texture and color.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mapmarker3dmodel#/s:7heresdk16MapMarker3DModelC18InstantiationErrora">`MapMarker3DModel.InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( mesh : Mesh , textureFilePath : String , color : UIColor ) throws
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mesh</code></em><code> </code></td>
  <td><div>
  <p>Mesh containing the 3d geometry together with texture coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textureFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to texture file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>Color to be blend with texture. This color is multiplied with color of texture.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(geometryFilePath: textureFilePath: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D model from path to .obj file and texture.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geometryFilePath : String , textureFilePath : String )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>geometryFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to obj file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textureFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to texture file.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(mesh: textureFilePath: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D model from mesh and texture.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mapmarker3dmodel#/s:7heresdk16MapMarker3DModelC18InstantiationErrora">`MapMarker3DModel.InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( mesh : Mesh , textureFilePath : String ) throws
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mesh</code></em><code> </code></td>
  <td><div>
  <p>Mesh containing the 3d geometry together with texture coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textureFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to texture file.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(geometryFilePath: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D model from path to .obj file.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geometryFilePath : String )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>geometryFilePath</code></em><code> </code></td>
  <td><div>
  <p>Absolute path to obj file.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(mesh: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D model from a mesh.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( mesh : Mesh )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mesh</code></em><code> </code></td>
  <td><div>
  <p>Mesh containing the 3d geometry 3D data.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarker3DModelC22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3dmodel#/s:7heresdk16MapMarker3DModelC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the reason for a failure to create <a href="sdk-for-ios-explore-classes-mapmarker3dmodel">`MapMarker3DModel`</a>.

  <a href="sdk-for-ios-explore-classes-mapmarker3dmodel-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapMarker3DModel.InstantiationErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

