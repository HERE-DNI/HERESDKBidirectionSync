---
title: "GPXDocument Class Reference"
slug: "sdk-for-ios-explore-classes-gpxdocument"
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

   <span id="sdk-for-ios-explore-s-7heresdk11GPXDocumentC11gpxFilePath7optionsACSS_AA10GPXOptionsVtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-gpxFilePath-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC11gpxFilePath7optionsACSS_AA10GPXOptionsVtKcfc" class="token"><code>init(gpxFilePath:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(gpxFilePath: String, options: GPXOptions) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-gpxoptions">GPXOptions</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk11GPXDocumentC6tracksACSayAA8GPXTrackCG_tcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-tracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC6tracksACSayAA8GPXTrackCG_tcfc" class="token"><code>init(tracks:</code><wbr></wbr><code>)</code></a> 

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
  public init(tracks: [GPXTrack])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-gpxtrack">GPXTrack</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tracks" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp" class="token"><code>tracks</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-classes-gpxtrack">GPXTrack</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11GPXDocumentC10fromString7content7optionsACSS_AA10GPXOptionsVtKFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-fromString-content-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC10fromString7content7optionsACSS_AA10GPXOptionsVtKFZ" class="token"><code>fromString(content:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromString(content: String, options: GPXOptions) throws -> GPXDocument
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-gpxoptions">GPXOptions</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-save-gpxFilePath" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF" class="token"><code>save(gpxFilePath:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Saves the document to a file. For saving the <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">`GPXDocument.tracks`</a> modification before writing to a file, use <a href="sdk-for-ios-explore-classes-gpxtrackwriter">`GPXTrackWriter`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func save(gpxFilePath: String) -> Bool
  ```

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

   <span id="sdk-for-ios-explore-s-7heresdk11GPXDocumentC8addTrack10trackToAddyAA8GPXTrackC_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addTrack-trackToAdd" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-gpxdocument#sdk-for-ios-explore-s-7heresdk11GPXDocumentC8addTrack10trackToAddyAA8GPXTrackC_tF" class="token"><code>addTrack(trackToAdd:</code><wbr></wbr><code>)</code></a> 

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
  public func addTrack(trackToAdd: GPXTrack)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-gpxtrack">GPXTrack</a>

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

