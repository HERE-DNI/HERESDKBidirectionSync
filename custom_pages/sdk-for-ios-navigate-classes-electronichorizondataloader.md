---
title: "ElectronicHorizonDataLoader Class Reference"
slug: "sdk-for-ios-navigate-classes-electronichorizondataloader"
---

# ElectronicHorizonDataLoader

<div class="declaration">

<div class="language">

``` highlight
public class ElectronicHorizonDataLoader
```

``` highlight
extension ElectronicHorizonDataLoader: NativeBase
```

``` highlight
extension ElectronicHorizonDataLoader: Hashable
```

</div>

</div>

Loads map data for segments that belong to the <a href="sdk-for-ios-navigate-classes-electronichorizonengine">`ElectronicHorizonEngine`</a> paths.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

Offline availability: This property is available online and offline.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC9sdkEngine7options07segmentD9CacheSizeAcA09SDKNativeG0C_AA07SegmentdE7OptionsVs5Int32VtKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-sdkEngine-options-segmentDataCacheSize" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-electronichorizondataloader#sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC9sdkEngine7options07segmentD9CacheSizeAcA09SDKNativeG0C_AA07SegmentdE7OptionsVs5Int32VtKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>options:</code><wbr></wbr><code>segmentDataCacheSize:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of `ElectronicHorizonDataLoader`. The constructor accepts options to configure the data loader. For more information, see <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions">`SegmentDataLoaderOptions`</a>. The cache size limits the number of segments that the loader can keep in memory at the same time.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> If the data loader cannot be created.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(sdkEngine: SDKNativeEngine, options: SegmentDataLoaderOptions, segmentDataCacheSize: Int32) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>

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
  <p>The <a href="sdk-for-ios-navigate-classes-sdknativeengine"><code>SDKNativeEngine</code></a> instance that provides shared services, such as networking and map data.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions"><code>SegmentDataLoaderOptions</code></a> instance that configures how segment data is requested.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>segmentDataCacheSize</code></em><code> </code></td>
  <td><div>
  <p>The maximum number of segments that the loader can cache.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC04loadD0010electronicC6UpdateyAA0bcH0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-loadData-electronicHorizonUpdate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-electronichorizondataloader#sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC04loadD0010electronicC6UpdateyAA0bcH0V_tF" class="token"><code>loadData(electronicHorizonUpdate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadData(electronicHorizonUpdate: ElectronicHorizonUpdate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-electronichorizonupdate">ElectronicHorizonUpdate</a>

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
  <td><code> </code><em><code>electronicHorizonUpdate</code></em><code> </code></td>
  <td><div>
  <p>The update that contains the segments to add to the cache and the segments to remove from the cache.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC10getSegment9segmentIdAA0bcdE6ResultVAA018DirectedOCMSegmentI0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getSegment-segmentId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-electronichorizondataloader#sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC10getSegment9segmentIdAA0bcdE6ResultVAA018DirectedOCMSegmentI0V_tF" class="token"><code>getSegment(segmentId:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns loaded data for the given segment identifier. The result contains either the loaded data or an error code.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getSegment(segmentId: DirectedOCMSegmentId) -> ElectronicHorizonDataLoaderResult
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-directedocmsegmentid">DirectedOCMSegmentId</a>
  - <a href="sdk-for-ios-navigate-structs-electronichorizondataloaderresult">ElectronicHorizonDataLoaderResult</a>

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
  <td><code> </code><em><code>segmentId</code></em><code> </code></td>
  <td><div>
  <p>The segment identifier for which to return the loaded data from the cache.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The result object that contains either the loaded segment data or an error code.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC03addbcdE14StatusDelegateyyAA0bcdegH0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-addElectronicHorizonDataLoaderStatusDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-electronichorizondataloader#sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC03addbcdE14StatusDelegateyyAA0bcdegH0_pF" class="token"><code>addElectronicHorizonDataLoaderStatusDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds an <a href="sdk-for-ios-navigate-protocols-electronichorizondataloaderstatusdelegate">`ElectronicHorizonDataLoaderStatusDelegate`</a> to the subscription list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addElectronicHorizonDataLoaderStatusDelegate(_ electronicHorizonListener: ElectronicHorizonDataLoaderStatusDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a>

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
  <td><code> </code><em><code>electronicHorizonListener</code></em><code> </code></td>
  <td><div>
  <p>The listener that receives data loader status updates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC06removebcdE14StatusDelegateyyAA0bcdegH0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeElectronicHorizonDataLoaderStatusDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-electronichorizondataloader#sdk-for-ios-navigate-s-7heresdk27ElectronicHorizonDataLoaderC06removebcdE14StatusDelegateyyAA0bcdegH0_pF" class="token"><code>removeElectronicHorizonDataLoaderStatusDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes an <a href="sdk-for-ios-navigate-protocols-electronichorizondataloaderstatusdelegate">`ElectronicHorizonDataLoaderStatusDelegate`</a> from the subscription list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeElectronicHorizonDataLoaderStatusDelegate(_ electronicHorizonListener: ElectronicHorizonDataLoaderStatusDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a>

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
  <td><code> </code><em><code>electronicHorizonListener</code></em><code> </code></td>
  <td><div>
  <p>The listener that should no longer receive data loader status updates.</p>
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

