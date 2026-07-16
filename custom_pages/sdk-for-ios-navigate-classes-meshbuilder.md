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
let cube = MeshBuilder()
    .quad(a: Point3D(x: 0.5, y: 0.5, z: 0.5),
          b: Point3D(x: -0.5, y: 0.5, z: 0.5),
          c: Point3D(x: 0.5, y: -0.5, z: 0.5),
          d: Point3D(x: -0.5, y: -0.5, z: 0.5))
    .quad(a: Point3D(x: -0.5, y: 0.5, z: -0.5),
          b: Point3D(x: 0.5, y: 0.5, z: -0.5),
          c: Point3D(x: -0.5, y: -0.5, z: -0.5),
          d: Point3D(x: 0.5, y: -0.5, z: -0.5))
    .quad(a: Point3D(x: 0.5, y: 0.5, z: -0.5),
          b: Point3D(x: 0.5, y: 0.5, z: 0.5),
          c: Point3D(x: 0.5, y: -0.5, z: -0.5),
          d: Point3D(x: 0.5, y: -0.5, z: 0.5))
    .quad(a: Point3D(x: -0.5, y: 0.5, z: 0.5),
          b: Point3D(x: -0.5, y: 0.5, z: -0.5),
          c: Point3D(x: -0.5, y: -0.5, z: 0.5),
          d: Point3D(x: -0.5, y: -0.5, z: -0.5))
    .quad(a: Point3D(x: -0.5, y: 0.5, z: 0.5),
          b: Point3D(x: 0.5, y: 0.5, z: 0.5),
          c: Point3D(x: -0.5, y: 0.5, z: -0.5),
          d: Point3D(x: 0.5, y: 0.5, z: -0.5))
    .quad(a: Point3D(x: 0.5, y: -0.5, z: 0.5),
          b: Point3D(x: -0.5, y: -0.5, z: 0.5),
          c: Point3D(x: 0.5, y: -0.5, z: -0.5),
          d: Point3D(x: -0.5, y: -0.5, z: -0.5))
    .build()
```

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MeshBuilderCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-meshbuilder#sdk-for-ios-navigate-s-7heresdk11MeshBuilderCACycfc" class="token"><code>init()</code></a> 

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
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MeshBuilderC8triangle1a1b1cAA08TrianglebC0CAA7Point3DV_A2KtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-triangle-a-b-c" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-meshbuilder#sdk-for-ios-navigate-s-7heresdk11MeshBuilderC8triangle1a1b1cAA08TrianglebC0CAA7Point3DV_A2KtF" class="token"><code>triangle(a:</code><wbr></wbr><code>b:</code><wbr></wbr><code>c:</code><wbr></wbr><code>)</code></a> 

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
  public func triangle(a: Point3D, b: Point3D, c: Point3D) -> TriangleMeshBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point3d">Point3D</a>
  - <a href="sdk-for-ios-navigate-classes-trianglemeshbuilder">TriangleMeshBuilder</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk11MeshBuilderC4quad1a1b1c1dAA04QuadbC0CAA7Point3DV_A3LtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-quad-a-b-c-d" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-meshbuilder#sdk-for-ios-navigate-s-7heresdk11MeshBuilderC4quad1a1b1c1dAA04QuadbC0CAA7Point3DV_A3LtF" class="token"><code>quad(a:</code><wbr></wbr><code>b:</code><wbr></wbr><code>c:</code><wbr></wbr><code>d:</code><wbr></wbr><code>)</code></a> 

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
  public func quad(a: Point3D, b: Point3D, c: Point3D, d: Point3D) -> QuadMeshBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point3d">Point3D</a>
  - <a href="sdk-for-ios-navigate-classes-quadmeshbuilder">QuadMeshBuilder</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk11MeshBuilderC5buildAA0B0CSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-meshbuilder#sdk-for-ios-navigate-s-7heresdk11MeshBuilderC5buildAA0B0CSgyF" class="token"><code>build()</code></a> 

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
  public func build() -> Mesh?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk4MeshC">Mesh</a>

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

