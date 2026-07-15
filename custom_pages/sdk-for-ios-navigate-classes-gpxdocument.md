---
title: "GPXDocument Class Reference"
slug: "sdk-for-ios-navigate-classes-gpxdocument"
---

# GPXDocument

<div class="declaration">

<div class="language">

``` highlight
public class GPXDocument
```

``` highlight
extension GPXDocument: NativeBase
```

``` highlight
extension GPXDocument: Hashable
```

</div>

</div>

Use the GPXDocument to load the GPX file. Only track data is used from the GPX file format (see trkType at <https://www.topografix.com/GPX/1/1/#type_trkType>). Any unknown elements in the file are ignored. Any known element with an invalid value returns an error. Elevation values are ignored.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(gpxFilePath: options: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a GPX document from a file.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( gpxFilePath : String , options : GPXOptions ) throws
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
  <td><code> </code><em><code>gpxFilePath</code></em><code> </code></td>
  <td><div>
  <p>The path to the GPX file.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options to customize reading.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(tracks: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a GPX document from a list of GPX tracks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( tracks : [ GPXTrack ])
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
  <td><code> </code><em><code>tracks</code></em><code> </code></td>
  <td><div>
  <p>The list of tracks.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp"></span>` `<span id="//apple_ref/swift/Property/tracks" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-gpxdocument#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp" class="token"><code>tracks</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The tracks stored in this GPX document.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tracks: [GPXTrack] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      fromString(content: options: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a GPX document from a string.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromString ( content : String , options : GPXOptions ) throws -> GPXDocument
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
  <td><code> </code><em><code>content</code></em><code> </code></td>
  <td><div>
  <p>The content of a GPX file as string.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options to customize reading.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An `GPXDocument` instance.

  </div>

  </div>

  </div>

- <div>

      save(gpxFilePath: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Saves the document to a file. For saving the <a href="sdk-for-ios-navigate-classes-gpxdocument#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">`GPXDocument.tracks`</a> modification before writing to a file, use <a href="sdk-for-ios-navigate-classes-gpxtrackwriter">`GPXTrackWriter`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func save ( gpxFilePath : String ) -> Bool
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
  <td><code> </code><em><code>gpxFilePath</code></em><code> </code></td>
  <td><div>
  <p>The file path where the GPX document will be saved.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `True` if the document has been saved successfully. `False` if an error has been happened during saving.

  </div>

  </div>

  </div>

- <div>

      addTrack(trackToAdd: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Add track to GPX document.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addTrack ( trackToAdd : GPXTrack )
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
  <td><code> </code><em><code>trackToAdd</code></em><code> </code></td>
  <td><div>
  <p>track to add to GPX document</p>
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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

