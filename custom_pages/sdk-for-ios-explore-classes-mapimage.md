---
title: "MapImage Class Reference"
slug: "sdk-for-ios-explore-classes-mapimage"
---

# MapImage

<div class="declaration">

<div class="language">

``` highlight
public class MapImage
```

``` highlight
extension MapImage: NativeBase
```

``` highlight
extension MapImage: Hashable
```

</div>

</div>

Represents a drawable resource that can be used by a <a href="sdk-for-ios-explore-classes-mapmarker">`MapMarker`</a>, <a href="sdk-for-ios-explore-classes-mapmarker3d">`MapMarker3D`</a> or <a href="sdk-for-ios-explore-classes-mapimageoverlay">`MapImageOverlay`</a> to be shown on the map. Supported formats are listed in <a href="sdk-for-ios-explore-enums-imageformat">`ImageFormat`</a>. SVG format allows custom fonts in text using font-family attribute by prior registration via `AssetsManager.registerFont`.

It is recommended to associate a resource with a single `MapImage` instance in order to enable resource sharing and reduce the amount of needed memory.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(pixelData: imageFormat: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new map image from the provided image data. Currently only <a href="sdk-for-ios-explore-enums-imageformat#/s:7heresdk11ImageFormatO3pngyA2CmF">`ImageFormat.png`</a> is accepted.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( pixelData : Data , imageFormat : ImageFormat )
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
  <td><code> </code><em><code>pixelData</code></em><code> </code></td>
  <td><div>
  <p>Data to be used for the image. The bytes of a PNG image datastream are expected as defined in <a href="https://www.w3.org/TR/PNG">https://www.w3.org/TR/PNG</a></p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>imageFormat</code></em><code> </code></td>
  <td><div>
  <p>The format of the image data to be used.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(imageData: imageFormat: width: height: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new map image from the provided image data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( imageData : Data , imageFormat : ImageFormat , width : UInt32 , height : UInt32 )
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
  <td><code> </code><em><code>imageData</code></em><code> </code></td>
  <td><div>
  <p>Data to be used for the image. For image format <a href="sdk-for-ios-explore-enums-imageformat#/s:7heresdk11ImageFormatO3svgyA2CmF"><code>ImageFormat.svg</code></a> the bytes of a UTF-8 encoded string in SVG Tiny format are expected. For the format specification see <a href="https://www.w3.org/TR/SVGTiny12">https://www.w3.org/TR/SVGTiny12</a></p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>imageFormat</code></em><code> </code></td>
  <td><div>
  <p>The format of the image data to be used.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>width</code></em><code> </code></td>
  <td><div>
  <p>The width of the image in pixels.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>height</code></em><code> </code></td>
  <td><div>
  <p>The height of the image in pixels.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(filePath: width: height: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new map image from the provided path to the SVG Tiny or PNG image.

  Will throw an error if either the height or width equals zero or the path is empty.

  Trying to load a file that is not compliant with SVG Tiny or PNG results in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG specification may result in an image that exhibits unexpected artifacts.

  The caller must ensure that the file remains accessible for the entire duration of its usage by the SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that remains accessible for the entire duration of its usage by the SDK or load and pass the file content to one of the `MapImage` constructors that creates instances out of image data (

      MapImage.init(Data, ImageFormat)

  ,
      MapImage.init(Data, ImageFormat, UInt32, UInt32)

  ).}
  </p>

  Please note that file paths that originate, for example from a file picker (like `UIDocumentPickerViewController`) can be deleted by the system while the application is still running.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( filePath : String , width : UInt32 , height : UInt32 ) throws
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
  <td><code> </code><em><code>filePath</code></em><code> </code></td>
  <td><div>
  <p>The path to image file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>width</code></em><code> </code></td>
  <td><div>
  <p>The width of image in pixels.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>height</code></em><code> </code></td>
  <td><div>
  <p>The height of image in pixels.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(from: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map image object from the supplied `UIImage` object. Throws an error if the supplied `UIImage` does not represent a regular image (for example, when it represents a mask).

  <div class="aside aside-throws">

  Throws

  `MapImage.InstantiationError` Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public convenience init ?( from uiImage : UIImage ) throws
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
  <td><code> </code><em><code>uiImage</code></em><code> </code></td>
  <td><div>
  <p>The image to use as source data.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(named: width: height: in: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map image object using a named image asset from the application’s main bundle or another bundle which can optionally be passed in. Currently only PNG or SVG Tiny image resources are supported.

  <div class="aside aside-throws">

  Throws

  `MapImage.InstantiationError` Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public convenience init ( named name : String , width : Int32 , height : Int32 , in bundle : Bundle ? = nil ) throws
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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>The name of the image asset.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>width</code></em><code> </code></td>
  <td><div>
  <p>Width of image in pixels</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>height</code></em><code> </code></td>
  <td><div>
  <p>Height of image in pixels</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bundle</code></em><code> </code></td>
  <td><div>
  <p>The bundle in which the asset resides. The main application bundle is used if not specified.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

