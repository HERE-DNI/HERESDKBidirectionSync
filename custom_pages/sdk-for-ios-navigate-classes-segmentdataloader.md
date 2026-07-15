---
title: "SegmentDataLoader Class Reference"
slug: "sdk-for-ios-navigate-classes-segmentdataloader"
---

# SegmentDataLoader

<div class="declaration">

<div class="language">

``` highlight
public class SegmentDataLoader
```

``` highlight
extension SegmentDataLoader: NativeBase
```

``` highlight
extension SegmentDataLoader: Hashable
```

</div>

</div>

Provides the protocol for the access to the segments data available in the local OCM map. Please be aware that the methods within this class load map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  Creates a new instance of this class.

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
  public init () throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(sdkEngine: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

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
  public init ( sdkEngine : SDKNativeEngine ) throws
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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>A SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getSegmentsAroundCoordinates(_: radiusInMeters: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Loads the segments around a certain coordinates. Returns an empty list in case no segments could be found around the coordinates.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-mapdata#/s:7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of a list of segments is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getSegmentsAroundCoordinates ( _ coordinates : GeoCoordinates , radiusInMeters : Double ) throws -> [ OCMSegmentId ]
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
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The location to explore</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>radiusInMeters</code></em><code> </code></td>
  <td><div>
  <p>The radius of the search. Only values between 1m and 5000m are accepted.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The list of segments around the given position. The segments are sorted by distance from the point. Throws if it’s not possible to return list of a list of segments.

  </div>

  </div>

  </div>

- <div>

      loadData(segment: options: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Synchronously load the data for the given map segment.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-mapdata#/s:7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of data of a segment is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadData ( segment : OCMSegmentId , options : SegmentDataLoaderOptions ) throws -> SegmentData
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
  <td><code> </code><em><code>segment</code></em><code> </code></td>
  <td><div>
  <p>The segment to load.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Request options</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Requested data of a segment.

  </div>

  </div>

  </div>

- <div>

      loadDirectedSegmentData(segment: options: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Synchronously load the data for the given map directed segment.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-mapdata#/s:7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of data of a segment is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadDirectedSegmentData ( segment : DirectedOCMSegmentId , options : SegmentDataLoaderOptions ) throws -> SegmentData
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
  <td><code> </code><em><code>segment</code></em><code> </code></td>
  <td><div>
  <p>The directed segment to load.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Request options</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Requested data of a segment.

  </div>

  </div>

  </div>

- <div>

      downloadFile(fileReferences: downloadingOptions: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Synchronously load the optional image providing guidance of a directed or non directed segment.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-mapdata#/s:7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of data of a segment is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func downloadFile ( fileReferences : [ FileReference ], downloadingOptions : DownloadingFileOptions ) throws -> [ Data ]
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
  <td><code> </code><em><code>fileReferences</code></em><code> </code></td>
  <td><div>
  <p>Provides information for a file reference.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>downloadingOptions</code></em><code> </code></td>
  <td><div>
  <p>Provides information regarding downloading configuration.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Requested data of a segment.

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

