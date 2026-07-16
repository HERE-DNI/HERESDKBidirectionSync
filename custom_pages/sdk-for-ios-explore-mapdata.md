---
title: "MapData  Reference"
slug: "sdk-for-ios-explore-mapdata"
---

# MapData

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19AdministrativeRulesV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-AdministrativeRules" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk19AdministrativeRulesV" class="token"><code>AdministrativeRules</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a set of administrative rules for a country or a state.

  <a href="sdk-for-ios-explore-structs-administrativerules" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AdministrativeRules : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk25AdministrativeRulesLoaderC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-AdministrativeRulesLoader" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk25AdministrativeRulesLoaderC" class="token"><code>AdministrativeRulesLoader</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the protocol for the access to the administrative rules available for a country or a state in the local OCM map. Please be aware that the methods within this classload map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-administrativerulesloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AdministrativeRulesLoader
  ```

  ``` highlight
  extension AdministrativeRulesLoader: NativeBase
  ```

  ``` highlight
  extension AdministrativeRulesLoader: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21AllowedTransportModesV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-AllowedTransportModes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk21AllowedTransportModesV" class="token"><code>AllowedTransportModes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies which transport modes are allowed in a particular direction.

  **Note:** This struct specifies a general restriction to that transport mode, but additional restriction are possible.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-allowedtransportmodes" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AllowedTransportModes : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24BloodAlcoholContentLimitV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-BloodAlcoholContentLimit" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk24BloodAlcoholContentLimitV" class="token"><code>BloodAlcoholContentLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the rules regarding alcohol in blood content limit in a country or state for all types of drivers.

  <a href="sdk-for-ios-explore-structs-bloodalcoholcontentlimit" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BloodAlcoholContentLimit : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12ConnectivityV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Connectivity" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk12ConnectivityV" class="token"><code>Connectivity</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information about link id and accessibility.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-connectivity" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Connectivity : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20DirectedOCMSegmentIdV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-DirectedOCMSegmentId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk20DirectedOCMSegmentIdV" class="token"><code>DirectedOCMSegmentId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  OCM Segment ID with travel direction of segment.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-directedocmsegmentid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DirectedOCMSegmentId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DownloadingFileOptionsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-DownloadingFileOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk22DownloadingFileOptionsV" class="token"><code>DownloadingFileOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct which identifies the configuration when downloading a file reference.

  <a href="sdk-for-ios-explore-structs-downloadingfileoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DownloadingFileOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11DrivingSideO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-DrivingSide" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk11DrivingSideO" class="token"><code>DrivingSide</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The side of the road on which the driving is done.

  <a href="sdk-for-ios-explore-enums-drivingside" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DrivingSide : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13FileReferenceV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-FileReference" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk13FileReferenceV" class="token"><code>FileReference</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a file reference.

  <a href="sdk-for-ios-explore-structs-filereference" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct FileReference : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17FileReferenceTypeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-FileReferenceType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk17FileReferenceTypeO" class="token"><code>FileReferenceType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of reference file.

  <a href="sdk-for-ios-explore-enums-filereferencetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum FileReferenceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21HeadlightsRequirementO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-HeadlightsRequirement" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk21HeadlightsRequirementO" class="token"><code>HeadlightsRequirement</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The situations in which headlights are required to be turned on.

  <a href="sdk-for-ios-explore-enums-headlightsrequirement" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum HeadlightsRequirement : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13LaneAttributeV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-LaneAttribute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk13LaneAttributeV" class="token"><code>LaneAttribute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that describes attributes assigned to a specific section of a lane. It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-laneattribute" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LaneAttribute : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk23LocalRoadCharacteristicO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-LocalRoadCharacteristic" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk23LocalRoadCharacteristicO" class="token"><code>LocalRoadCharacteristic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the local road characteristics: frontage, parking lot road, poi access.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-localroadcharacteristic" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocalRoadCharacteristic : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapDataLoaderErrora"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-MapDataLoaderError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk18MapDataLoaderErrora" class="token"><code>MapDataLoaderError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error occurred during obtaining data form the map. <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode">`MapDataLoaderErrorCode`</a> represents possible errors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapDataLoaderError = MapDataLoaderErrorCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode">MapDataLoaderErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22MapDataLoaderErrorCodeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-MapDataLoaderErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk22MapDataLoaderErrorCodeO" class="token"><code>MapDataLoaderErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors from map data accessing.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapDataLoaderErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapDataLoaderErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12OCMSegmentIdV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-OCMSegmentId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk12OCMSegmentIdV" class="token"><code>OCMSegmentId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  OCM Segment ID of particular matched <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> from OCM map, represented in form: Tile + Local ID’s .

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-ocmsegmentid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct OCMSegmentId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21ParkingSideRegulationO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-ParkingSideRegulation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk21ParkingSideRegulationO" class="token"><code>ParkingSideRegulation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The regulations for parking on the side of the road.

  <a href="sdk-for-ios-explore-enums-parkingsideregulation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ParkingSideRegulation : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-PhysicalAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV" class="token"><code>PhysicalAttributes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Physical attributes of the segment.

  ***Note*** a road can have more than one attribute at the same time.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-physicalattributes" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PhysicalAttributes : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PreTripPlanningV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-PreTripPlanning" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk15PreTripPlanningV" class="token"><code>PreTripPlanning</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the legal requirements to be considered before a trip for all vehicles types.

  <a href="sdk-for-ios-explore-structs-pretripplanning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PreTripPlanning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15RailwayCrossingV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-RailwayCrossing" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk15RailwayCrossingV" class="token"><code>RailwayCrossing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies the presence and the location of railway corssings. Included in <a href="sdk-for-ios-explore-classes-segmentdata">`SegmentData`</a> only if <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions#sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">`SegmentDataLoaderOptions.loadRailwayCrossings`</a> is set to `true`.

  <a href="sdk-for-ios-explore-structs-railwaycrossing" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RailwayCrossing
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RailwayCrossingTypeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-RailwayCrossingType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk19RailwayCrossingTypeO" class="token"><code>RailwayCrossingType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of railway crossing.

  <a href="sdk-for-ios-explore-enums-railwaycrossingtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RailwayCrossingType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11RoadDividerO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-RoadDivider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk11RoadDividerO" class="token"><code>RoadDivider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-roaddivider" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RoadDivider : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10RoadUsagesV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-RoadUsages" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk10RoadUsagesV" class="token"><code>RoadUsages</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road Usages of the segment.

  ***Note*** a road can have more than one attribute at the same time.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-roadusages" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RoadUsages : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21SegmentConnectivitiesV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-SegmentConnectivities" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk21SegmentConnectivitiesV" class="token"><code>SegmentConnectivities</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information about segment one direction source and target connectivities.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentconnectivities" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentConnectivities : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-SegmentData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC" class="token"><code>SegmentData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the requested information for a segment

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentdata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentData
  ```

  ``` highlight
  extension SegmentData: NativeBase
  ```

  ``` highlight
  extension SegmentData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-SegmentDataLoader" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC" class="token"><code>SegmentDataLoader</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the protocol for the access to the segments data available in the local OCM map. Please be aware that the methods within this class load map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentdataloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-SegmentDataLoaderOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV" class="token"><code>SegmentDataLoaderOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies which data should be loaded by the <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadData(...)`</a> or <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a> function.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentDataLoaderOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk25SegmentReferenceConverterC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-SegmentReferenceConverter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk25SegmentReferenceConverterC" class="token"><code>SegmentReferenceConverter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A SegmentReferenceConverter provides possibility to convert mapmatched instances of <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> to corresponding instances of <a href="sdk-for-ios-explore-structs-directedocmsegmentid">`DirectedOCMSegmentId`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentreferenceconverter" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentReferenceConverter
  ```

  ``` highlight
  extension SegmentReferenceConverter: NativeBase
  ```

  ``` highlight
  extension SegmentReferenceConverter: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15SegmentSpanDataC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-SegmentSpanData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk15SegmentSpanDataC" class="token"><code>SegmentSpanData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains attributes that are not necessarily constant on a full segment. A Span is a portion of a Segment where the requested attributes are constant.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-segmentspandata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SegmentSpanData
  ```

  ``` highlight
  extension SegmentSpanData: NativeBase
  ```

  ``` highlight
  extension SegmentSpanData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28SegmentSpecialSpeedSituationV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-SegmentSpecialSpeedSituation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk28SegmentSpecialSpeedSituationV" class="token"><code>SegmentSpecialSpeedSituation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A special speed situation indicates a speed that exists under special circumstances. It can be used to further refine the estimation of traversal times, route calculation and calculation of route guidance timing.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentspecialspeedsituation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentSpecialSpeedSituation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17SegmentSpeedLimitV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-SegmentSpeedLimit" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk17SegmentSpeedLimitV" class="token"><code>SegmentSpeedLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the posted speed limit on the segment span.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-segmentspeedlimit" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SegmentSpeedLimit : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16SpecialSpeedTypeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-SpecialSpeedType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk16SpecialSpeedTypeO" class="token"><code>SpecialSpeedType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the speed situation type.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-specialspeedtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum SpecialSpeedType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TollCostV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TollCost" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk8TollCostV" class="token"><code>TollCost</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains informations about the toll costs for a specific vehicle profile.

  <a href="sdk-for-ios-explore-structs-tollcost" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollCost : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TollPointV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TollPoint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk9TollPointV" class="token"><code>TollPoint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct to represent the toll point attributes of a segment.

  <a href="sdk-for-ios-explore-structs-tollpoint" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollPoint
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TollStructureV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TollStructure" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk13TollStructureV" class="token"><code>TollStructure</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that defines tolling configuration for a lane. It describes which types of toll structures apply and the acceptable payment methods. This information can be used to guide drivers through toll roads based on their preferences or vehicle capabilities.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-tollstructure" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollStructure : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21TollStructureManeuverV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TollStructureManeuver" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk21TollStructureManeuverV" class="token"><code>TollStructureManeuver</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a toll structure at a toll point.

  <a href="sdk-for-ios-explore-structs-tollstructuremaneuver" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollStructureManeuver
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17TollStructureTypeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TollStructureType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk17TollStructureTypeO" class="token"><code>TollStructureType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum defines the type of toll structure used on a road segment or lane. Each value represents a different tolling mechanism used in road infrastructure. This enum helps in providing detailed tolling information for routing and navigation.

  <a href="sdk-for-ios-explore-enums-tollstructuretype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TollStructureType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10TollSystemV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TollSystem" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk10TollSystemV" class="token"><code>TollSystem</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains informations about a toll system.

  <a href="sdk-for-ios-explore-structs-tollsystem" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollSystem : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficSignalV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TrafficSignal" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk13TrafficSignalV" class="token"><code>TrafficSignal</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies the presence and the location of traffic lights at an intersection

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-trafficsignal" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficSignal
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21TrafficSignalLocationO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TrafficSignalLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk21TrafficSignalLocationO" class="token"><code>TrafficSignalLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the location of a traffic signal.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-trafficsignallocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficSignalLocation : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TurnOnRedRegulationO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TurnOnRedRegulation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-mapdata#sdk-for-ios-explore-s-7heresdk19TurnOnRedRegulationO" class="token"><code>TurnOnRedRegulation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The regulations for turning on the red color of the traffic light.

  <a href="sdk-for-ios-explore-enums-turnonredregulation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TurnOnRedRegulation : UInt32, CaseIterable, Codable
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

