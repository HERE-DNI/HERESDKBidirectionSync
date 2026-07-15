---
title: "ElectronicHorizon  Reference"
slug: "sdk-for-ios-explore-electronichorizon"
---

# ElectronicHorizon

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17ElectronicHorizonV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizon" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk17ElectronicHorizonV" class="token"><code>ElectronicHorizon</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct containing the full set of available paths predicted for the current vehicle state.

  Represents a snapshot of the horizon estimation at the moment the update was generated.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizon" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizon : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ElectronicHorizonDataLoaderC"></span>` `<span id="//apple_ref/swift/Class/ElectronicHorizonDataLoader" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk27ElectronicHorizonDataLoaderC" class="token"><code>ElectronicHorizonDataLoader</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Loads map data for segments that belong to the <a href="sdk-for-ios-explore-classes-electronichorizonengine">`ElectronicHorizonEngine`</a> paths.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  Offline availability: This property is available online and offline.

  <a href="sdk-for-ios-explore-classes-electronichorizondataloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk36ElectronicHorizonDataLoaderErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/ElectronicHorizonDataLoaderErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk36ElectronicHorizonDataLoaderErrorCodeO" class="token"><code>ElectronicHorizonDataLoaderErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents error codes that describe the result of the

      ElectronicHorizonDataLoader.getSegment(...)

  method.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  Offline availability: This property is available online and offline.

  <a href="sdk-for-ios-explore-enums-electronichorizondataloadererrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ElectronicHorizonDataLoaderErrorCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ElectronicHorizonDataLoaderResultV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonDataLoaderResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk33ElectronicHorizonDataLoaderResultV" class="token"><code>ElectronicHorizonDataLoaderResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the result of a data loading operation performed by <a href="sdk-for-ios-explore-classes-electronichorizondataloader">`ElectronicHorizonDataLoader`</a>. The result contains either the loaded segment data or an error code.

  Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizondataloaderresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonDataLoaderResult
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ElectronicHorizonDataLoadedStatusO"></span>` `<span id="//apple_ref/swift/Enum/ElectronicHorizonDataLoadedStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk33ElectronicHorizonDataLoadedStatusO" class="token"><code>ElectronicHorizonDataLoadedStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the status of data that was loaded by <a href="sdk-for-ios-explore-classes-electronichorizondataloader">`ElectronicHorizonDataLoader`</a>.

  <a href="sdk-for-ios-explore-enums-electronichorizondataloadedstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ElectronicHorizonDataLoadedStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk41ElectronicHorizonDataLoaderStatusDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/ElectronicHorizonDataLoaderStatusDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk41ElectronicHorizonDataLoaderStatusDelegateP" class="token"><code>ElectronicHorizonDataLoaderStatusDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a delegate for status updates from the

      ElectronicHorizonDataLoader.loadData(...)

  method. The listener receives the current state for different levels of the paths as <a href="sdk-for-ios-explore-enums-electronichorizondataloadedstatus">`ElectronicHorizonDataLoadedStatus`</a>.
  </p>

  Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  Offline availability: This property is available online and offline.

  <a href="sdk-for-ios-explore-protocols-electronichorizondataloaderstatusdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol ElectronicHorizonDataLoaderStatusDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25ElectronicHorizonDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/ElectronicHorizonDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk25ElectronicHorizonDelegateP" class="token"><code>ElectronicHorizonDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a delegate for receiving updates during execution of the

      ElectronicHorizonEngine.update(...)

  method.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  Offline availability: This property is available online and offline.

  <a href="sdk-for-ios-explore-protocols-electronichorizondelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol ElectronicHorizonDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23ElectronicHorizonEngineC"></span>` `<span id="//apple_ref/swift/Class/ElectronicHorizonEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk23ElectronicHorizonEngineC" class="token"><code>ElectronicHorizonEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight. You can subscribe to electronic horizon updates based on position updates by using <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a>. For more information about sub path levels, see <a href="sdk-for-ios-explore-structs-electronichorizonoptions#/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMetersSaySdGvp">`ElectronicHorizonOptions.lookAheadDistancesInMeters`</a>.

  The electronic horizon engine uses map-matched locations and can optionally use a <a href="sdk-for-ios-explore-classes-route">`Route`</a> to improve the most-preferred path (MPP).

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-electronichorizonengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class ElectronicHorizonEngine
  ```

  ``` highlight
  extension ElectronicHorizonEngine: NativeBase
  ```

  ``` highlight
  extension ElectronicHorizonEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26ElectronicHorizonErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/ElectronicHorizonErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk26ElectronicHorizonErrorCodeO" class="token"><code>ElectronicHorizonErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents error codes that describe the result of the

      ElectronicHorizonEngine.update(...)

  method.
  </p>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  Offline availability: This property is available online and offline.

  <a href="sdk-for-ios-explore-enums-electronichorizonerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ElectronicHorizonErrorCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24ElectronicHorizonOptionsV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk24ElectronicHorizonOptionsV" class="token"><code>ElectronicHorizonOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides options to configure <a href="sdk-for-ios-explore-classes-electronichorizonengine">`ElectronicHorizonEngine`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21ElectronicHorizonPathV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonPath" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk21ElectronicHorizonPathV" class="token"><code>ElectronicHorizonPath</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a single electronic horizon path.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonpath" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonPath : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25ElectronicHorizonPositionV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonPosition" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk25ElectronicHorizonPositionV" class="token"><code>ElectronicHorizonPosition</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a position on an electronic horizon path with a reference to the current item in the <a href="sdk-for-ios-explore-structs-electronichorizon">`ElectronicHorizon`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonposition" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonPosition : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24ElectronicHorizonSegmentV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonSegment" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk24ElectronicHorizonSegmentV" class="token"><code>ElectronicHorizonSegment</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a segment in an <a href="sdk-for-ios-explore-structs-electronichorizonpath">`ElectronicHorizonPath`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonsegment" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonSegment : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31ElectronicHorizonSegmentChangesV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonSegmentChanges" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk31ElectronicHorizonSegmentChangesV" class="token"><code>ElectronicHorizonSegmentChanges</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct describing the set of changes in horizon segments between two consecutive updates. Includes lists of both newly added and removed segments.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonsegmentchanges" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonSegmentChanges : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26ElectronicHorizonSegmentIdV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonSegmentId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk26ElectronicHorizonSegmentIdV" class="token"><code>ElectronicHorizonSegmentId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a segment in an <a href="sdk-for-ios-explore-structs-electronichorizonpath">`ElectronicHorizonPath`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonsegmentid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonSegmentId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23ElectronicHorizonUpdateV"></span>` `<span id="//apple_ref/swift/Struct/ElectronicHorizonUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-electronichorizon#/s:7heresdk23ElectronicHorizonUpdateV" class="token"><code>ElectronicHorizonUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct representing a full update delivered via <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a> notifications.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-electronichorizonupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ElectronicHorizonUpdate : Hashable
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

