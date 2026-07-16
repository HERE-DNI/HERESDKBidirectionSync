---
title: "SegmentDataLoader Class Reference"
slug: "sdk-for-ios-explore-classes-segmentdataloader"
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

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderCACyKcfc" class="token"><code>init()</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC9sdkEngineAcA09SDKNativeF0C_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC9sdkEngineAcA09SDKNativeF0C_tKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(sdkEngine: SDKNativeEngine) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC28getSegmentsAroundCoordinates_14radiusInMetersSayAA12OCMSegmentIdVGAA03GeoH0V_SdtKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getSegmentsAroundCoordinates-_-radiusInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC28getSegmentsAroundCoordinates_14radiusInMetersSayAA12OCMSegmentIdVGAA03GeoH0V_SdtKF" class="token"><code>getSegmentsAroundCoordinates(_:</code><wbr></wbr><code>radiusInMeters:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of a list of segments is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getSegmentsAroundCoordinates(_ coordinates: GeoCoordinates, radiusInMeters: Double) throws -> [OCMSegmentId]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-ocmsegmentid">OCMSegmentId</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-loadData-segment-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF" class="token"><code>loadData(segment:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of data of a segment is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadData(segment: OCMSegmentId, options: SegmentDataLoaderOptions) throws -> SegmentData
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-ocmsegmentid">OCMSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>
  - <a href="sdk-for-ios-explore-classes-segmentdata">SegmentData</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-loadDirectedSegmentData-segment-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF" class="token"><code>loadDirectedSegmentData(segment:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of data of a segment is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadDirectedSegmentData(segment: DirectedOCMSegmentId, options: SegmentDataLoaderOptions) throws -> SegmentData
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-directedocmsegmentid">DirectedOCMSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>
  - <a href="sdk-for-ios-explore-classes-segmentdata">SegmentData</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC12downloadFile14fileReferences18downloadingOptionsSay10Foundation0C0VGSayAA0F9ReferenceVG_AA011DownloadingfJ0VtKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-downloadFile-fileReferences-downloadingOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC12downloadFile14fileReferences18downloadingOptionsSay10Foundation0C0VGSayAA0F9ReferenceVG_AA011DownloadingfJ0VtKF" class="token"><code>downloadFile(fileReferences:</code><wbr></wbr><code>downloadingOptions:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk18MapDataLoaderErrora">`MapDataLoaderError`</a> Specifies reason, why list of data of a segment is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func downloadFile(fileReferences: [FileReference], downloadingOptions: DownloadingFileOptions) throws -> [Data]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-filereference">FileReference</a>
  - <a href="sdk-for-ios-explore-structs-downloadingfileoptions">DownloadingFileOptions</a>

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

