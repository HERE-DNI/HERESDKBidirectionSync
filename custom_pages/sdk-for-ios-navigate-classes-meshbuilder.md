---
title: "MeshBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-meshbuilder"
---

# MeshBuilder

<div class="declaration">

<div class="language">

``` highlight
public class MeshBuilder
```

``` highlight
extension MeshBuilder: NativeBase
```

``` highlight
extension MeshBuilder: Hashable
```

</div>

</div>

Builder for meshes. Such meshes can contain different kinds of primitives, like quads or triangles. Both primitives support adding texture coordinates that are mapped to the corners of the primitives. See <a href="sdk-for-ios-navigate-classes-trianglemeshbuilder">`TriangleMeshBuilder`</a> and <a href="sdk-for-ios-navigate-classes-quadmeshbuilder">`QuadMeshBuilder`</a> for more details.

Note: Normals cannot be set as they are not necessary when using the `MeshBuilder`.

**Example how to build a cube using <a href="sdk-for-ios-navigate-classes-quadmeshbuilder">`QuadMeshBuilder`</a>**

``` highlight
let cube = MeshBuilder () . quad ( a : Point3D ( x : 0.5 , y : 0.5 , z : 0.5 ), b : Point3D ( x : - 0.5 , y : 0.5 , z : 0.5 ), c : Point3D ( x : 0.5 , y : - 0.5 , z : 0.5 ), d : Point3D ( x : - 0.5 , y : - 0.5 , z : 0.5 )) . quad ( a : Point3D ( x : - 0.5 , y : 0.5 , z : - 0.5 ), b : Point3D ( x : 0.5 , y : 0.5 , z : - 0.5 ), c : Point3D ( x : - 0.5 , y : - 0.5 , z : - 0.5 ), d : Point3D ( x : 0.5 , y : - 0.5 , z : - 0.5 )) . quad ( a : Point3D ( x : 0.5 , y : 0.5 , z : - 0.5 ), b : Point3D ( x : 0.5 , y : 0.5 , z : 0.5 ), c : Point3D ( x : 0.5 , y : - 0.5 , z : - 0.5 ), d : Point3D ( x : 0.5 , y : - 0.5 , z : 0.5 )) . quad ( a : Point3D ( x : - 0.5 , y : 0.5 , z : 0.5 ), b : Point3D ( x : - 0.5 , y : 0.5 , z : - 0.5 ), c : Point3D ( x : - 0.5 , y : - 0.5 , z : 0.5 ), d : Point3D ( x : - 0.5 , y : - 0.5 , z : - 0.5 )) . quad ( a : Point3D ( x : - 0.5 , y : 0.5 , z : 0.5 ), b : Point3D ( x : 0.5 , y : 0.5 , z : 0.5 ), c : Point3D ( x : - 0.5 , y : 0.5 , z : - 0.5 ), d : Point3D ( x : 0.5 , y : 0.5 , z : - 0.5 )) . quad ( a : Point3D ( x : 0.5 , y : - 0.5 , z : 0.5 ), b : Point3D ( x : - 0.5 , y : - 0.5 , z : 0.5 ), c : Point3D ( x : 0.5 , y : - 0.5 , z : - 0.5 ), d : Point3D ( x : - 0.5 , y : - 0.5 , z : - 0.5 )) . build ()
```

</pre>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an instance of MeshBuilder.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      triangle(a: b: c: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a triangle.

  Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have counter-clockwise winding.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func triangle ( a : Point3D , b : Point3D , c : Point3D ) -> TriangleMeshBuilder
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
  <td><code> </code><em><code>a</code></em><code> </code></td>
  <td><div>
  <p>First vertex of the triangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>b</code></em><code> </code></td>
  <td><div>
  <p>Second vertex of the triangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>c</code></em><code> </code></td>
  <td><div>
  <p>Third vertex of the triangle.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A <a href="sdk-for-ios-navigate-classes-trianglemeshbuilder">`TriangleMeshBuilder`</a> instance.

  </div>

  </div>

  </div>

- <div>

      quad(a: b: c: d: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a quad. Internally, this will be transformed into triangles abc and bdc.

  Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have counter-clockwise winding.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func quad ( a : Point3D , b : Point3D , c : Point3D , d : Point3D ) -> QuadMeshBuilder
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
  <td><code> </code><em><code>a</code></em><code> </code></td>
  <td><div>
  <p>First vertex of quad.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>b</code></em><code> </code></td>
  <td><div>
  <p>Second vertex of the quad.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>c</code></em><code> </code></td>
  <td><div>
  <p>Third vertex of the quad.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>d</code></em><code> </code></td>
  <td><div>
  <p>Fourth vertex of the quad.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A <a href="sdk-for-ios-navigate-classes-quadmeshbuilder">`QuadMeshBuilder`</a> instance.

  </div>

  </div>

  </div>

- <div>

      build()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build () -> Mesh ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  mesh containing added geometry or ‘null’ if no geometry was added.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

