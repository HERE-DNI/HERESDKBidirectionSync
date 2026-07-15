---
title: "Navigation  Reference"
slug: "sdk-for-ios-navigate-navigation"
---

# Navigation

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC"></span>` `<span id="//apple_ref/swift/Class/AreaCameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk18AreaCameraBehaviorC" class="token"><code>AreaCameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use this class to show an overview of geo points. By default, the orientation of the camera will be perpendicular to the Earth’s surface (ie. looking towards the center of the Earth), while bearing will be towards north.

  Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-areacamerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AreaCameraBehavior : CameraBehavior
  ```

  ``` highlight
  extension AreaCameraBehavior: NativeBase
  ```

  ``` highlight
  extension AreaCameraBehavior: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25ArrivalNotificationOptionO"></span>` `<span id="//apple_ref/swift/Enum/ArrivalNotificationOption" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk25ArrivalNotificationOptionO" class="token"><code>ArrivalNotificationOption</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates arrival point type to announce in maneuver notification.

  <a href="sdk-for-ios-navigate-enums-arrivalnotificationoption" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ArrivalNotificationOption : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11AspectRatioO"></span>` `<span id="//apple_ref/swift/Enum/AspectRatio" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk11AspectRatioO" class="token"><code>AspectRatio</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The aspect ratio of the image.

  <a href="sdk-for-ios-navigate-enums-aspectratio" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum AspectRatio : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC"></span>` `<span id="//apple_ref/swift/Class/AutomotiveCameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24AutomotiveCameraBehaviorC" class="token"><code>AutomotiveCameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors. This class acts as a facade, delegating camera operations to either a <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> for following the vehicle during navigation or an <a href="sdk-for-ios-navigate-classes-areacamerabehavior">`AreaCameraBehavior`</a> for showing overview areas such as points of interest or route previews.

  The controller supports three states: tracking mode (following the vehicle), area mode (showing geographic regions), or inactive (no automatic camera control). The inactive state allows external control of the camera, such as when responding to user touch events or when UI logic temporarily disables automatic camera behavior.

  Camera configuration, including animation durations, zoom policies, and maneuver handling settings, can be provided through a JSON configuration string or file. The configuration is validated and parsed during construction.

  Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AutomotiveCameraBehavior : CameraBehavior
  ```

  ``` highlight
  extension AutomotiveCameraBehavior: NativeBase
  ```

  ``` highlight
  extension AutomotiveCameraBehavior: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18BorderCrossingTypeO"></span>` `<span id="//apple_ref/swift/Enum/BorderCrossingType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk18BorderCrossingTypeO" class="token"><code>BorderCrossingType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of a border crossing given in a <a href="sdk-for-ios-navigate-structs-bordercrossingwarning">`BorderCrossingWarning`</a>.

  <a href="sdk-for-ios-navigate-enums-bordercrossingtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum BorderCrossingType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21BorderCrossingWarningV"></span>` `<span id="//apple_ref/swift/Struct/BorderCrossingWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21BorderCrossingWarningV" class="token"><code>BorderCrossingWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A border crossing. The main field describing the border crossing is <a href="sdk-for-ios-navigate-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">`BorderCrossingWarning.type`</a> specifying whether the border crossing is given for a country border or a state border. The <a href="sdk-for-ios-navigate-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">`BorderCrossingWarning.type`</a> must be known. The country and state codes are contained in <a href="sdk-for-ios-navigate-structs-bordercrossingwarning#/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp">`BorderCrossingWarning.administrativeRules`</a> along with other information such as speed limits, u-turn regulations or pre-trip planning information contained by the <a href="sdk-for-ios-navigate-structs-administrativerules">`AdministrativeRules`</a>.

  Use `BorderCrossingWarningListener` to get notifications about upcoming country or state border crossings.

  <a href="sdk-for-ios-navigate-structs-bordercrossingwarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BorderCrossingWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29BorderCrossingWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/BorderCrossingWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk29BorderCrossingWarningDelegateP" class="token"><code>BorderCrossingWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive border crossing warnings for country and state borders. **Note:** The border crossing warner is a point warner, which means that for a border crossing there will *always* be 2 warnings emitted, with the \[BorderCrossingWarning.distance_type\] set to <a href="sdk-for-ios-navigate-enums-distancetype#/s:7heresdk12DistanceTypeO5aheadyA2CmF">`DistanceType.ahead`</a> and <a href="sdk-for-ios-navigate-enums-distancetype#/s:7heresdk12DistanceTypeO6passedyA2CmF">`DistanceType.passed`</a> which is given when the location of the border crossing is reached. A <a href="sdk-for-ios-navigate-structs-bordercrossingwarning">`BorderCrossingWarning`</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-ios-navigate-structs-bordercrossingwarning">`BorderCrossingWarning`</a> 120 meters and <a href="sdk-for-ios-navigate-structs-bordercrossingwarning">`BorderCrossingWarning`</a> 160 meters ahead, the first \[BorderCrossingWarning.distance_to_border_crossing_in_meters\] is 120 meters and the next \[BorderCrossingWarning.distance_to_border_crossing_in_meters\] is then 40 meters, since that is the distance between the first and second warnings.

  <a href="sdk-for-ios-navigate-protocols-bordercrossingwarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol BorderCrossingWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28BorderCrossingWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/BorderCrossingWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk28BorderCrossingWarningOptionsV" class="token"><code>BorderCrossingWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Border crossing warning options.

  <a href="sdk-for-ios-navigate-structs-bordercrossingwarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BorderCrossingWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14CameraBehaviorP"></span>` `<span id="//apple_ref/swift/Protocol/CameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk14CameraBehaviorP" class="token"><code>CameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol used to change implement different camera behaviors.

  <a href="sdk-for-ios-navigate-protocols-camerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CameraBehavior : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV"></span>` `<span id="//apple_ref/swift/Struct/CurrentSituationLaneView" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24CurrentSituationLaneViewV" class="token"><code>CurrentSituationLaneView</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides current situation lane assistance view information for the street at the current position of a single lane.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-currentsituationlaneview" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CurrentSituationLaneView : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk34CurrentSituationLaneAssistanceViewV"></span>` `<span id="//apple_ref/swift/Struct/CurrentSituationLaneAssistanceView" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk34CurrentSituationLaneAssistanceViewV" class="token"><code>CurrentSituationLaneAssistanceView</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides current situation lane assistance view information for the street at the current location.

  <a href="sdk-for-ios-navigate-structs-currentsituationlaneassistanceview" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CurrentSituationLaneAssistanceView : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk42CurrentSituationLaneAssistanceViewDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/CurrentSituationLaneAssistanceViewDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk42CurrentSituationLaneAssistanceViewDelegateP" class="token"><code>CurrentSituationLaneAssistanceViewDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications on <a href="sdk-for-ios-navigate-structs-currentsituationlaneassistanceview">`CurrentSituationLaneAssistanceView`</a>.

  The current situation lane assistance view notifications describe the lane information at the current location.

  A new notification is evaluated with each location update. A notification is only sent when there is a change in lane data, such as a new upcoming lane.

  This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode. During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route to reach the destination. However, the event does not indicate which exact lane the user is currently driving in. The listener works for offline mode as well.

  **Note:**

  - Lane information is not available for all roads. It’s mostly available for roads with painted turn directions.
  - This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-currentsituationlaneassistanceviewdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CurrentSituationLaneAssistanceViewDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CustomPanningDataV"></span>` `<span id="//apple_ref/swift/Struct/CustomPanningData" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17CustomPanningDataV" class="token"><code>CustomPanningData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class contains all the information regarding the next angular panning element, including a new estimated audio cue duration, and a new set of initial and sweep angular angle, allowing the customization of the spatial audio trajectories for any type of notification, such as speed or merge warners, maneuvers or even roundabouts notifications. The orientation in space for <a href="sdk-for-ios-navigate-structs-custompanningdata#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">`CustomPanningData.initialAzimuthInDegrees`</a> and <a href="sdk-for-ios-navigate-structs-custompanningdata#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">`CustomPanningData.sweepAzimuthInDegrees`</a> can be represented by the following angular values:

  | Front | Right |  Rear  | Left |
  |:-----:|:-----:|:------:|:----:|
  |  0°   | +90°  | +- 180 | -90° |

  When any of the members of `CustomPanningData` are initialized as null, the default value provided by HERE SDK will be used instead. The audio cue is spatialized considering the action of both maneuvers, for example, the audio cue ‘Now turn right and then turn left’ will be spatialized as following: ‘Now turn right’ will be heard as coming from the right. ‘and then turn left’ will be heard as coming from the left. Note: The estimation for playing both audio cues could be not fully accurate and therefore a mismatch between the audio source and the audio cue message could be perceived.

  <a href="sdk-for-ios-navigate-structs-custompanningdata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CustomPanningData : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17DangerZoneWarningV"></span>` `<span id="//apple_ref/swift/Struct/DangerZoneWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17DangerZoneWarningV" class="token"><code>DangerZoneWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents danger zones. A danger zone refers to areas where there is an increased risk of traffic incidents. These zones are designated to alert drivers to potential hazards and encourage safer driving behaviors. Legally, certain devices can alert you to being in a danger zone, typically indicating the presence of a speed camera. In line with applicable law and industry standard, these alerts are usually provided along a road within a range of 4 km on a motorway, 2 km outside built-up areas, and 300 m in built-up areas​​. The HERE SDK warns when approaching the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or more speed cameras in it. The exact location of such speed cameras is not provided. Note that danger zones are only available in selected countries, such as France.

  <a href="sdk-for-ios-navigate-structs-dangerzonewarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DangerZoneWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25DangerZoneWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/DangerZoneWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk25DangerZoneWarningDelegateP" class="token"><code>DangerZoneWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about the Danger zones.

  <a href="sdk-for-ios-navigate-protocols-dangerzonewarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DangerZoneWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26DestinationReachedDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/DestinationReachedDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26DestinationReachedDelegateP" class="token"><code>DestinationReachedDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications from this class about the arrival at the destination.

  <a href="sdk-for-ios-navigate-protocols-destinationreacheddelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DestinationReachedDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DimensionRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/DimensionRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20DimensionRestrictionV" class="token"><code>DimensionRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a dimension restriction.

  <a href="sdk-for-ios-navigate-structs-dimensionrestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DimensionRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24DimensionRestrictionTypeO"></span>` `<span id="//apple_ref/swift/Enum/DimensionRestrictionType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24DimensionRestrictionTypeO" class="token"><code>DimensionRestrictionType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the type of a dimension restriction.

  <a href="sdk-for-ios-navigate-enums-dimensionrestrictiontype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DimensionRestrictionType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31DirectionInformationUsageOptionO"></span>` `<span id="//apple_ref/swift/Enum/DirectionInformationUsageOption" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk31DirectionInformationUsageOptionO" class="token"><code>DirectionInformationUsageOption</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the option of direction information included in the notification.

  <a href="sdk-for-ios-navigate-enums-directioninformationusageoption" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DirectionInformationUsageOption : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12DistanceTypeO"></span>` `<span id="//apple_ref/swift/Enum/DistanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk12DistanceTypeO" class="token"><code>DistanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** The distance types are being given for warnings at distances which can be configured via options specific for each warner. These distances are defined based on the `sdk.navigation.TimingProfile` calculated based on the speed limit present at the driver’s current location. Indicates the distance type for a warning.

  <a href="sdk-for-ios-navigate-enums-distancetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DistanceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13DividerMarkerO"></span>` `<span id="//apple_ref/swift/Enum/DividerMarker" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk13DividerMarkerO" class="token"><code>DividerMarker</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the divider between the lanes.

  <a href="sdk-for-ios-navigate-enums-dividermarker" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DividerMarker : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21DynamicCameraBehaviorC"></span>` `<span id="//apple_ref/swift/Class/DynamicCameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21DynamicCameraBehaviorC" class="token"><code>DynamicCameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use this class to follow the current location of the user: The camera will look at the target location that was fed into the navigator instance, gradually zooming in as the user approaches each maneuver and zooming out after the user passes them. Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement. If no route is set, constant values of camera distance and tilt are used.

  <a href="sdk-for-ios-navigate-classes-dynamiccamerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DynamicCameraBehavior : CameraBehavior
  ```

  ``` highlight
  extension DynamicCameraBehavior: NativeBase
  ```

  ``` highlight
  extension DynamicCameraBehavior: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC"></span>` `<span id="//apple_ref/swift/Class/DynamicRoutingEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20DynamicRoutingEngineC" class="token"><code>DynamicRoutingEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class queries the HERE routing backend to find routes with less traffic and therefore an earlier remaining estimated time of arrival.

  `DynamicRoutingEngine` polls the HERE routing backend periodically to find the best new route out of a given initial route. For initial route calculation it is recommended to use the <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> as it already requests traffic-optimized routes.

  When a better route is found, it is recommended to follow these steps to set the new route:

  1.  Stop the `DynamicRoutingEngine`.

  2.  Update the currently active <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>instance with the newly found route.

  3.  Restart the `DynamicRoutingEngine`. This should be done outside of the

          onBetterRouteFound()

      callback.

  For both `DynamicRoutingEngine` and <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a>, the resulting routes are optimized based on speed flow changes such as traffic jams, street closures or road accidents. To get the best result, it is recommended to not specify the <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">`RouteOptions.departureTime`</a> as then the current time is used by default.

  The poll interval is defined by <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions#/s:7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">`DynamicRoutingEngineOptions.pollInterval`</a> and triggered by

      DynamicRoutingEngine.updateCurrentLocation(...)

  .
  </p>

  <a href="sdk-for-ios-navigate-classes-dynamicroutingengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DynamicRoutingEngine
  ```

  ``` highlight
  extension DynamicRoutingEngine: NativeBase
  ```

  ``` highlight
  extension DynamicRoutingEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22DynamicRoutingDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/DynamicRoutingDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk22DynamicRoutingDelegateP" class="token"><code>DynamicRoutingDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about the new route via the <a href="sdk-for-ios-navigate-classes-dynamicroutingengine">`DynamicRoutingEngine`</a>.

  <a href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DynamicRoutingDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27DynamicRoutingEngineOptionsV"></span>` `<span id="//apple_ref/swift/Struct/DynamicRoutingEngineOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27DynamicRoutingEngineOptionsV" class="token"><code>DynamicRoutingEngineOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options defining the behavior of the <a href="sdk-for-ios-navigate-classes-dynamicroutingengine">`DynamicRoutingEngine`</a>. Both, `minTimeDifference` and `minTimeDifferencePercentage`, will be checked: When the poll interval is reached, the smaller difference will win and the <a href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate">`DynamicRoutingDelegate`</a> is notified.

  <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DynamicRoutingEngineOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EnvironmentalZoneWarningV"></span>` `<span id="//apple_ref/swift/Struct/EnvironmentalZoneWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24EnvironmentalZoneWarningV" class="token"><code>EnvironmentalZoneWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents Environmental zones.

  <a href="sdk-for-ios-navigate-structs-environmentalzonewarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EnvironmentalZoneWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk32EnvironmentalZoneWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/EnvironmentalZoneWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk32EnvironmentalZoneWarningDelegateP" class="token"><code>EnvironmentalZoneWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about the environmental zones.

  <a href="sdk-for-ios-navigate-protocols-environmentalzonewarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol EnvironmentalZoneWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EventTextV"></span>` `<span id="//apple_ref/swift/Struct/EventText" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk9EventTextV" class="token"><code>EventText</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains all the information regarding the next text announcement.

  <a href="sdk-for-ios-navigate-structs-eventtext" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EventText : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EventTextDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/EventTextDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17EventTextDelegateP" class="token"><code>EventTextDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications when text notifications are available from <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>. Multiple notifications can be given for the same maneuver at different distances.

  <a href="sdk-for-ios-navigate-protocols-eventtextdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol EventTextDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EventTextOptionsV"></span>` `<span id="//apple_ref/swift/Struct/EventTextOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk16EventTextOptionsV" class="token"><code>EventTextOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Text notifications options.

  <a href="sdk-for-ios-navigate-structs-eventtextoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EventTextOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19FixedCameraBehaviorC"></span>` `<span id="//apple_ref/swift/Class/FixedCameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19FixedCameraBehaviorC" class="token"><code>FixedCameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use this class to follow the current location of the user: The camera will permanently look at the target location that was fed into the navigator instance. Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement.

  <a href="sdk-for-ios-navigate-classes-fixedcamerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class FixedCameraBehavior : CameraBehavior
  ```

  ``` highlight
  extension FixedCameraBehavior: NativeBase
  ```

  ``` highlight
  extension FixedCameraBehavior: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26GeneralWarningRoadSignTypeO"></span>` `<span id="//apple_ref/swift/Enum/GeneralWarningRoadSignType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26GeneralWarningRoadSignTypeO" class="token"><code>GeneralWarningRoadSignType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of a general warning that a road sign represents.

  <a href="sdk-for-ios-navigate-enums-generalwarningroadsigntype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum GeneralWarningRoadSignType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GPXDocumentC"></span>` `<span id="//apple_ref/swift/Class/GPXDocument" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk11GPXDocumentC" class="token"><code>GPXDocument</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use the GPXDocument to load the GPX file. Only track data is used from the GPX file format (see trkType at <https://www.topografix.com/GPX/1/1/#type_trkType>). Any unknown elements in the file are ignored. Any known element with an invalid value returns an error. Elevation values are ignored.

  <a href="sdk-for-ios-navigate-classes-gpxdocument" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10GPXOptionsV"></span>` `<span id="//apple_ref/swift/Struct/GPXOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk10GPXOptionsV" class="token"><code>GPXOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used when reading the GPX file.

  <a href="sdk-for-ios-navigate-structs-gpxoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GPXOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8GPXTrackC"></span>` `<span id="//apple_ref/swift/Class/GPXTrack" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk8GPXTrackC" class="token"><code>GPXTrack</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Single track from the <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a>. Can be used as an input to the <a href="sdk-for-ios-navigate-classes-locationsimulator">`LocationSimulator`</a>. Can be created and modified via <a href="sdk-for-ios-navigate-classes-gpxtrackwriter">`GPXTrackWriter`</a>.

  <a href="sdk-for-ios-navigate-classes-gpxtrack" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class GPXTrack
  ```

  ``` highlight
  extension GPXTrack: NativeBase
  ```

  ``` highlight
  extension GPXTrack: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14GPXTrackWriterC"></span>` `<span id="//apple_ref/swift/Class/GPXTrackWriter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk14GPXTrackWriterC" class="token"><code>GPXTrackWriter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Writes GPX track points to <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>. The instance of the class should be added as a listener to the <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a> for GPX track recording. Appends the new location to the back segment of the track whenever the listener is called. The following data (if provided) can be recorded and inserted into the resulting <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>: `latitude, longitude, altitude, time, bearingInDegrees, pitchInDegrees, speedInMetersPerSecond, horizontalAccuracyInMeters, verticalAccuracyInMeters, bearingAccuracyInDegrees, speedAccuracyInMetersPerSecond` and `locationTechnology`.

  Use case examples:

  A user wants to create and save a new <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> with one <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>:

  - create `GPXTrackWriter` and add it as a location listener to <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>.

  - set user parameters to <a href="sdk-for-ios-navigate-classes-gpxtrackwriter#/s:7heresdk14GPXTrackWriterC5trackAA0B0Cvp">`GPXTrackWriter.track`</a> (e.g. <a href="sdk-for-ios-navigate-classes-gpxtrack#/s:7heresdk8GPXTrackC4nameSSvp">`GPXTrack.name`</a> or <a href="sdk-for-ios-navigate-classes-gpxtrack#/s:7heresdk8GPXTrackC11descriptionSSvp">`GPXTrack.description`</a>).

  - when writing is completed, create a new <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> with a list of one <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a> and save the document via

        GPXDocument.save(...)

    .

  A user wants to modify and save <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a> in the existing <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a>:

  - load <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> from a file by the relevant constructor.

  - create `GPXTrackWriter` with the required track in the list <a href="sdk-for-ios-navigate-classes-gpxdocument#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">`GPXDocument.tracks`</a>, add the created instance as a location listener to <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>.

  - when writing is completed, save the document via

        GPXDocument.save(...)

    .

  The <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.

  <a href="sdk-for-ios-navigate-classes-gpxtrackwriter" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class GPXTrackWriter : LocationDelegate
  ```

  ``` highlight
  extension GPXTrackWriter: NativeBase
  ```

  ``` highlight
  extension GPXTrackWriter: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28InterpolatedLocationDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/InterpolatedLocationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk28InterpolatedLocationDelegateP" class="token"><code>InterpolatedLocationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive interpolated locations. The interpolated locations are only provided between

      VisualNavigator.startRendering(...)

  and
      VisualNavigator.stopRendering(...)

  calls and the application is not running in the background.
  </p>

  <a href="sdk-for-ios-navigate-protocols-interpolatedlocationdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol InterpolatedLocationDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26JunctionViewLaneAssistanceV"></span>` `<span id="//apple_ref/swift/Struct/JunctionViewLaneAssistance" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26JunctionViewLaneAssistanceV" class="token"><code>JunctionViewLaneAssistance</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides lane assistance information for the next complex junction in order to keep following the route. It is recommended to indicate `JunctionViewLaneAssistance` and <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> separately or to indicate only <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> information - `JunctionViewLaneAssistance` will recommend all lanes that allow to pass the upcoming complex junction, regardless if they will lead to the next maneuver or not. If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be the same as the ones from <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a>.

  A junction is recognized as complex only if:

  - it is at least a bifurcation;
  - it has at least two lanes whose directions do not follow the current route. In opposition to <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a>, notifications are also forwarded when there is no maneuver action occurring at the next complex junction. Therefore, `JunctionViewLaneAssistance` can be disjointed from maneuvers. If lane assistance should be used to associate it with upcoming maneuvers, consider to use <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> instead. Note that <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> notifications are synchronized with maneuver events, whereas `JunctionViewLaneAssistance` events are not strictly synchronized with maneuver events.

  <a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct JunctionViewLaneAssistance : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk34JunctionViewLaneAssistanceDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/JunctionViewLaneAssistanceDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk34JunctionViewLaneAssistanceDelegateP" class="token"><code>JunctionViewLaneAssistanceDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications on <a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance">`JunctionViewLaneAssistance`</a>. See <a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance">`JunctionViewLaneAssistance`</a> documentation for further details.

  <a href="sdk-for-ios-navigate-protocols-junctionviewlaneassistancedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol JunctionViewLaneAssistanceDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4LaneV"></span>` `<span id="//apple_ref/swift/Struct/Lane" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk4LaneV" class="token"><code>Lane</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a lane.

  <a href="sdk-for-ios-navigate-structs-lane" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Lane : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV"></span>` `<span id="//apple_ref/swift/Struct/LaneAccess" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk10LaneAccessV" class="token"><code>LaneAccess</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct which identifies the vehicle type(s) allowed to access a lane.

  <a href="sdk-for-ios-navigate-structs-laneaccess" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LaneAccess : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13LaneDirectionO"></span>` `<span id="//apple_ref/swift/Enum/LaneDirection" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk13LaneDirectionO" class="token"><code>LaneDirection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum defines the lane direction.

  <a href="sdk-for-ios-navigate-enums-lanedirection" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LaneDirection : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21LaneDirectionCategoryV"></span>` `<span id="//apple_ref/swift/Struct/LaneDirectionCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21LaneDirectionCategoryV" class="token"><code>LaneDirectionCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the directions of a lane. Most lanes lead only to one direction, but there can be also lanes that split up into multiple directions. A road can consist of multiple lanes towards the same direction. Note: All members can be `true` or `false` at the same time. Lanes such as bicycle lanes mostly never contain a direction category and thus, all members are `false`.

  <a href="sdk-for-ios-navigate-structs-lanedirectioncategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LaneDirectionCategory : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12LaneMarkingsV"></span>` `<span id="//apple_ref/swift/Struct/LaneMarkings" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk12LaneMarkingsV" class="token"><code>LaneMarkings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for the lane markings.

  Lane markings indicate the markings on the road.

  Lane Divider Marker indicates the lane separator on the right side of the specified lane in the lane driving direction for Right-side driving countries. For left-sided driving countries the Lane Divider Marker is indicating the lane separator on the left side of the specified lane in the lane driving direction.

  <a href="sdk-for-ios-navigate-structs-lanemarkings" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LaneMarkings : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23LaneRecommendationStateO"></span>` `<span id="//apple_ref/swift/Enum/LaneRecommendationState" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk23LaneRecommendationStateO" class="token"><code>LaneRecommendationState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether this lane leads to the next maneuvers or not. The next maneuver is the next upcoming maneuver which is not yet reached, but that was already announced as *new* maneuver in \[sdk.navigation.RouteProgress.maneuver_progress\].

  <a href="sdk-for-ios-navigate-enums-lanerecommendationstate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LaneRecommendationState : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV"></span>` `<span id="//apple_ref/swift/Struct/LaneType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk8LaneTypeV" class="token"><code>LaneType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information on the available lane properties. The lane type values can be combined as follows:

  - High Occupancy Vehicle, Reversible
  - High Occupancy Vehicle and Express
  - Reversible and Express
  - High Occupancy Vehicle, Reversible and Express
  - High Occupancy Vehicle and Acceleration
  - Reversible, Acceleration Lane
  - High Occupancy Vehicle, Reversible, Acceleration Lane
  - Express and Acceleration
  - High Occupancy Vehicle and Deceleration
  - Reversible, Deceleration Lane
  - High Occupancy Vehicle, Reversible, Deceleration Lane
  - Express and Deceleration

  <a href="sdk-for-ios-navigate-structs-lanetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LaneType : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LowSpeedZoneWarningV"></span>` `<span id="//apple_ref/swift/Struct/LowSpeedZoneWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19LowSpeedZoneWarningV" class="token"><code>LowSpeedZoneWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides low speed zone. The main field describing the low speed zone is `LowSpeedZoneWarning.speed_limit_in_meters_per_second` specifying the speed limit of the low speed zone. Use `LowSpeedZoneWarningListener` to get notifications about upcoming low speed zones.

  <a href="sdk-for-ios-navigate-structs-lowspeedzonewarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LowSpeedZoneWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27LowSpeedZoneWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/LowSpeedZoneWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27LowSpeedZoneWarningDelegateP" class="token"><code>LowSpeedZoneWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive low speed zone warnings. **Note:** This is currently available *only* for Japan. The low speed zone warner is a zone warner, which means that for a low speed zone there will *always* be 3 warnings emitted, with the `LowSpeedZoneWarning.distance_type` set to `DistanceType.AHEAD, DistanceType.REACHED` and lastly `DistanceType.PASSED` when the end of the low speed zone is passed.

  <a href="sdk-for-ios-navigate-protocols-lowspeedzonewarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LowSpeedZoneWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ManeuverNotificationDetailsV"></span>` `<span id="//apple_ref/swift/Struct/ManeuverNotificationDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27ManeuverNotificationDetailsV" class="token"><code>ManeuverNotificationDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides the information regarding the next maneuver to be triggered

  <a href="sdk-for-ios-navigate-structs-maneuvernotificationdetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverNotificationDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ManeuverNotificationOptionsV"></span>` `<span id="//apple_ref/swift/Struct/ManeuverNotificationOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27ManeuverNotificationOptionsV" class="token"><code>ManeuverNotificationOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct containing all options to be used when generating maneuver notifications.

  <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverNotificationOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33ManeuverNotificationTimingOptionsV"></span>` `<span id="//apple_ref/swift/Struct/ManeuverNotificationTimingOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk33ManeuverNotificationTimingOptionsV" class="token"><code>ManeuverNotificationTimingOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct defining timing and distance thresholds for maneuver notifications.

  Setting custom values will impact the time when the notification for each supported <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">`ManeuverNotificationType`</a> is sent - dependent on the <a href="sdk-for-ios-navigate-enums-timingprofile">`TimingProfile`</a>.

  **Note:** By default, notification thresholds depend on <a href="sdk-for-ios-navigate-enums-timingprofile">`TimingProfile`</a>. When custom values are set, then these rules will still apply. The following rules apply for all transport modes:

  - For <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> timing profile will be used instead.
  - For <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">`TimingProfile.regularSpeed`</a> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> timing profile will be used instead.
  - For <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">`TimingProfile.slowSpeed`</a> timing profile the thresholds will be always used as specified.

  The timings follow a strict order:

  1.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).
  2.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">`ManeuverNotificationType.reminder`</a>: The second notification.
  3.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a>: A second reminder notification to take action.
  4.  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a>: Final notification, specifying the required action to be taken.

  Therefore, it is crucial that the set values do not violate the order: range \> reminder \> distance \> action. For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400. If <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> is smaller than <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters`</a> the new options will be silently ignored and the previous values are kept.

  You always have the choice to specify the thresholds for time or distance. For each <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">`ManeuverNotificationType`</a> a notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time and distance values. A configuration value of 0 is only allowed for <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters`</a> and <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">`ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`</a>. It means that the maneuver notifications of type <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">`ManeuverNotificationType.range`</a> should be generated as soon as the maneuver location is known - no matter how far away it may be. It’s impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.

  You can also specify the <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions#/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp">`ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters`</a> threshold that determines the distance between two maneuvers that should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this threshold will be merged like in this example: “After 300 meters turn right and then turn left.”.

  Tip: To set the timings to the HERE SDK, you can first call

      getManeuverNotificationTimingOptions()

  to get the default values for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the
      setManeuverNotificationTimingOptions()

  .
  </p>

  Note: In the comment of each attribute, the term `Others` refers to non-pedestrian transport modes such as <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO7bicycleyA2CmF">`TransportMode.bicycle`</a>, <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>.

  Attention: The default values for <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO10pedestrianyA2CmF">`TransportMode.pedestrian`</a> on <a href="sdk-for-ios-navigate-enums-timingprofile#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">`TimingProfile.fastSpeed`</a> are theoretical, as such routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.

  Usage example:

  ``` highlight
  // Get current values or default values, if no values have been set before. ManeuverNotificationTimingOptions car_highway_timings = Navigator . getManeuverNotificationTimingOptions ( TransportMode . car , TimingProfile . FAST_SPEED ); // Set a new value for a specific option and keep the previous or default values for the others. car_highway_timings . distanceNotificationDistanceInMeters = 1500 ; // Apply the changes to Navigator (or VisualNavigator). Navigator . setManeuverNotificationTimingOptions ( TransportMode . car , TimingProfile . FAST_SPEED , car_fast_speed_timings );
  ```

  </pre>

  <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverNotificationTimingOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24ManeuverNotificationTypeO"></span>` `<span id="//apple_ref/swift/Enum/ManeuverNotificationType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24ManeuverNotificationTypeO" class="token"><code>ManeuverNotificationType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the type of the maneuver notification.

  <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ManeuverNotificationType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16ManeuverProgressV"></span>` `<span id="//apple_ref/swift/Struct/ManeuverProgress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk16ManeuverProgressV" class="token"><code>ManeuverProgress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a user’s progress to a <a href="sdk-for-ios-navigate-classes-maneuver">`Maneuver`</a>.

  <a href="sdk-for-ios-navigate-structs-maneuverprogress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverProgress : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26ManeuverViewLaneAssistanceV"></span>` `<span id="//apple_ref/swift/Struct/ManeuverViewLaneAssistance" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26ManeuverViewLaneAssistanceV" class="token"><code>ManeuverViewLaneAssistance</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides lane assistance information for the next maneuver(s). During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes in order to complete the upcoming maneuvers. The notifications are synchronized with the <a href="sdk-for-ios-navigate-protocols-eventtextdelegate">`EventTextDelegate`</a>. <a href="sdk-for-ios-navigate-protocols-eventtextdelegate">`EventTextDelegate`</a> has 4 notification types for each maneuver: Range, Reminder, Distance and Action. Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object (e.g. “After 400 meters, turn right onto Invalidenstraße”). The notification will not be sent when other types of maneuver notification are given. The notification will not be sent when no lane data is available. During tracking mode, no notifications are delivered. This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.

  <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverViewLaneAssistance : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk34ManeuverViewLaneAssistanceDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/ManeuverViewLaneAssistanceDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk34ManeuverViewLaneAssistanceDelegateP" class="token"><code>ManeuverViewLaneAssistanceDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications on <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a>. See <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> documentation for further details.

  <a href="sdk-for-ios-navigate-protocols-maneuverviewlaneassistancedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol ManeuverViewLaneAssistanceDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV"></span>` `<span id="//apple_ref/swift/Struct/MapMatchedLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk18MapMatchedLocationV" class="token"><code>MapMatchedLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a map-matched location in the world at a given time.

  <a href="sdk-for-ios-navigate-structs-mapmatchedlocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapMatchedLocation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MilestoneV"></span>` `<span id="//apple_ref/swift/Struct/Milestone" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk9MilestoneV" class="token"><code>Milestone</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents information about the waypoints along the route.

  Note that this can include additional waypoints added during route calculation that may not have been part of the original user-defined waypoint list. For example, additional waypoints are added automatically between sections that require a different transport mode like when taking a ferry.

  <a href="sdk-for-ios-navigate-structs-milestone" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Milestone : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MilestoneStatusO"></span>` `<span id="//apple_ref/swift/Enum/MilestoneStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk15MilestoneStatusO" class="token"><code>MilestoneStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents the status of the <a href="sdk-for-ios-navigate-structs-milestone">`Milestone`</a>.

  <a href="sdk-for-ios-navigate-enums-milestonestatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MilestoneStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23MilestoneStatusDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/MilestoneStatusDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk23MilestoneStatusDelegateP" class="token"><code>MilestoneStatusDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications from this class about the arrival at each <a href="sdk-for-ios-navigate-structs-milestone">`Milestone`</a> or missing it.

  <a href="sdk-for-ios-navigate-protocols-milestonestatusdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MilestoneStatusDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13MilestoneTypeO"></span>` `<span id="//apple_ref/swift/Enum/MilestoneType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk13MilestoneTypeO" class="token"><code>MilestoneType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents the type of the <a href="sdk-for-ios-navigate-structs-milestone">`Milestone`</a>.

  <a href="sdk-for-ios-navigate-enums-milestonetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MilestoneType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19NaturalGuidanceTypeO"></span>` `<span id="//apple_ref/swift/Enum/NaturalGuidanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19NaturalGuidanceTypeO" class="token"><code>NaturalGuidanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the type of the natural guidance element.

  <a href="sdk-for-ios-navigate-enums-naturalguidancetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum NaturalGuidanceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17NavigableLocationV"></span>` `<span id="//apple_ref/swift/Struct/NavigableLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17NavigableLocationV" class="token"><code>NavigableLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains all the relevant information on the current location.

  <a href="sdk-for-ios-navigate-structs-navigablelocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NavigableLocation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25NavigableLocationDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/NavigableLocationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk25NavigableLocationDelegateP" class="token"><code>NavigableLocationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about the current location from <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>.

  <a href="sdk-for-ios-navigate-protocols-navigablelocationdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol NavigableLocationDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC"></span>` `<span id="//apple_ref/swift/Class/Navigator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk9NavigatorC" class="token"><code>Navigator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides the basic navigation functionality. It provides notifications about current map-matched location updates (see <a href="sdk-for-ios-navigate-structs-navigablelocation">`NavigableLocation`</a>). And, if a route has been set, about the route progress (see <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a>), route deviations (see <a href="sdk-for-ios-navigate-structs-routedeviation">`RouteDeviation`</a>) and maneuver notifications (see <a href="sdk-for-ios-navigate-protocols-eventtextdelegate">`EventTextDelegate`</a>).

  All transport modes are supported for turn-by-turn navigation, except for public transit. Public transit routes may lead to unsafe and unexpected results.

  Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and turn-by-turn bus instructions may not be as appropriate as expected.

  The <a href="sdk-for-ios-navigate-enums-transportmode">`TransportMode`</a> is determined from the provided <a href="sdk-for-ios-navigate-classes-route">`Route`</a> instance, but the actual <a href="sdk-for-ios-navigate-enums-sectiontransportmode">`SectionTransportMode`</a> can vary along a route, for example, when a ferry must be taken. When no route is set, the <a href="sdk-for-ios-navigate-structs-navigablelocation">`NavigableLocation`</a> assumes a drive scenario.

  This class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-ios-navigate-protocols-locationdelegate">`LocationDelegate`</a>. The accuracy of the positioning increases with the update frequency. At least one update per second should be provided. More information can be found at `LocationAccuracy.NAVIGATION`.

  **Note:** Even without provided locations, for example, while driving through a tunnel, this class can interpolate missing location events and still send <a href="sdk-for-ios-navigate-structs-navigablelocation">`NavigableLocation`</a>, <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a> and maneuver notifications.

  <a href="sdk-for-ios-navigate-classes-navigator" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Navigator : NavigatorProtocol
  ```

  ``` highlight
  extension Navigator: NativeBase
  ```

  ``` highlight
  extension Navigator: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17NavigatorProtocolP"></span>` `<span id="//apple_ref/swift/Protocol/NavigatorProtocol" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17NavigatorProtocolP" class="token"><code>NavigatorProtocol</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol provides the basic functionality needed to run a navigation session.

  <a href="sdk-for-ios-navigate-protocols-navigatorprotocol" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol NavigatorProtocol : LocationDelegate
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24NotificationFormatOptionO"></span>` `<span id="//apple_ref/swift/Enum/NotificationFormatOption" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24NotificationFormatOptionO" class="token"><code>NotificationFormatOption</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the formatting option of phoneme included in the notification.

  <a href="sdk-for-ios-navigate-enums-notificationformatoption" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum NotificationFormatOption : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33OffRoadDestinationReachedDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/OffRoadDestinationReachedDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk33OffRoadDestinationReachedDelegateP" class="token"><code>OffRoadDestinationReachedDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications from this class about the arrival at the off-road destination.

  <a href="sdk-for-ios-navigate-protocols-offroaddestinationreacheddelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol OffRoadDestinationReachedDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15OffRoadProgressV"></span>` `<span id="//apple_ref/swift/Struct/OffRoadProgress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk15OffRoadProgressV" class="token"><code>OffRoadProgress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the information needed to help the users to reach their off-road destination.

  <a href="sdk-for-ios-navigate-structs-offroadprogress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct OffRoadProgress : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23OffRoadProgressDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/OffRoadProgressDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk23OffRoadProgressDelegateP" class="token"><code>OffRoadProgressDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about the current off-road location from <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>.

  <a href="sdk-for-ios-navigate-protocols-offroadprogressdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol OffRoadProgressDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24RealisticViewRasterImageV"></span>` `<span id="//apple_ref/swift/Struct/RealisticViewRasterImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24RealisticViewRasterImageV" class="token"><code>RealisticViewRasterImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A realistic view. The fields describing the realistic view are <a href="sdk-for-ios-navigate-structs-realisticviewrasterimage#/s:7heresdk24RealisticViewRasterImageV09realisticc3PngE7Content10Foundation4DataVvp">`RealisticViewRasterImage.realisticViewPngImageContent`</a> contains a PNG image of the realistic view and is represented as binary data. `RealisticViewRasterImage.realisticViewType` indicates the type of the realistic view. A valid realistic view contains a non-empty <a href="sdk-for-ios-navigate-structs-realisticviewrasterimage#/s:7heresdk24RealisticViewRasterImageV09realisticc3PngE7Content10Foundation4DataVvp">`RealisticViewRasterImage.realisticViewPngImageContent`</a>. Use `RealisticViewWarningListener` to get notifications with the realistic views of the upcoming realistic view.

  <a href="sdk-for-ios-navigate-structs-realisticviewrasterimage" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RealisticViewRasterImage : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24RealisticViewVectorImageV"></span>` `<span id="//apple_ref/swift/Struct/RealisticViewVectorImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24RealisticViewVectorImageV" class="token"><code>RealisticViewVectorImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A realistic view of a junction. The fields describing the realistic view are <a href="sdk-for-ios-navigate-structs-realisticviewvectorimage#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">`RealisticViewVectorImage.junctionViewSvgImageContent`</a> contains a SVG image of the junction view represented as a string. <a href="sdk-for-ios-navigate-structs-realisticviewvectorimage#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">`RealisticViewVectorImage.signpostSvgImageContent`</a> contains an SVG image of the signpost corresponding to the junction, also represented as a string. A valid realistic view contains a non-empty <a href="sdk-for-ios-navigate-structs-realisticviewvectorimage#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">`RealisticViewVectorImage.junctionViewSvgImageContent`</a> and a non-empty <a href="sdk-for-ios-navigate-structs-realisticviewvectorimage#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">`RealisticViewVectorImage.signpostSvgImageContent`</a>. Use `RealisticViewWarningListener` to get notifications with the realistic views of the upcoming junctions.

  <a href="sdk-for-ios-navigate-structs-realisticviewvectorimage" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RealisticViewVectorImage : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RealisticViewWarningV"></span>` `<span id="//apple_ref/swift/Struct/RealisticViewWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20RealisticViewWarningV" class="token"><code>RealisticViewWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A realistic view notification. This notification is given for complex junctions and it includes a visual representation of that junction, in order to help the user to better navigate it. When <a href="sdk-for-ios-navigate-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">`RealisticViewWarning.distanceType`</a> is <a href="sdk-for-ios-navigate-enums-distancetype#/s:7heresdk12DistanceTypeO5aheadyA2CmF">`DistanceType.ahead`</a>, the <a href="sdk-for-ios-navigate-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewVectorImage`</a> object will be provided with the junction view and the signpost representations. For <a href="sdk-for-ios-navigate-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">`RealisticViewWarning.distanceType`</a> with value <a href="sdk-for-ios-navigate-enums-distancetype#/s:7heresdk12DistanceTypeO6passedyA2CmF">`DistanceType.passed`</a>, the <a href="sdk-for-ios-navigate-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewVectorImage`</a> object will be null. Use `RealisticViewWarningListener` to get notifications about the realistic views of the upcoming junctions.

  Realistic view notifications require an online connection in order to function properly, or that the junction or signpost map layer data is cached, installed or preloaded as part of a <a href="sdk-for-ios-navigate-structs-region">`Region`</a>. This can be enabled via feature configurations.

  <a href="sdk-for-ios-navigate-structs-realisticviewwarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RealisticViewWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28RealisticViewWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RealisticViewWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk28RealisticViewWarningDelegateP" class="token"><code>RealisticViewWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive realistic view warnings.

  A <a href="sdk-for-ios-navigate-structs-realisticviewwarning">`RealisticViewWarning`</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-ios-navigate-structs-realisticviewwarning">`RealisticViewWarning`</a> 120 meters and <a href="sdk-for-ios-navigate-structs-realisticviewwarning">`RealisticViewWarning`</a> 160 meters ahead, the first <a href="sdk-for-ios-navigate-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp">`RealisticViewWarning.distanceToRealisticViewInMeters`</a> is 120 meters and the next <a href="sdk-for-ios-navigate-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp">`RealisticViewWarning.distanceToRealisticViewInMeters`</a> is then 40 meters, since that is the distance between the first and second warnings.

  <a href="sdk-for-ios-navigate-protocols-realisticviewwarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RealisticViewWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27RealisticViewWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/RealisticViewWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27RealisticViewWarningOptionsV" class="token"><code>RealisticViewWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Realistic view warning options. Set the options for filtering the realistic view notifications and setting the realistic view notification distances based on the road type.

  <a href="sdk-for-ios-navigate-structs-realisticviewwarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RealisticViewWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RailwayCrossingWarningV"></span>` `<span id="//apple_ref/swift/Struct/RailwayCrossingWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk22RailwayCrossingWarningV" class="token"><code>RailwayCrossingWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides railway crossing. The main field describing the railway crossing is <a href="sdk-for-ios-navigate-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp">`RailwayCrossingWarning.type`</a> specifying whether the railway crossing is protected by a barrier or not. Use `RailwayCrossingWarningListener` to get notifications about upcoming railway crossings.

  <a href="sdk-for-ios-navigate-structs-railwaycrossingwarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RailwayCrossingWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30RailwayCrossingWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RailwayCrossingWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk30RailwayCrossingWarningDelegateP" class="token"><code>RailwayCrossingWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive railway crossing warnings. **Note:** The railway crossing warner can be either a zone warner or a point warner, depending on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad crossing is a zone warner then 3 warnings will be emitted with the `RailwayCrossingWarning.distance_type` set to `DistanceType.AHEAD, DistanceType.REACHED` and lastly `DistanceType.PASSED` when the end of the railway crossing is passed. In case the railroad crossing is a point warner then 2 warnings will be emitted with the `RailwayCrossingWarning.distance_type` set to `DistanceType.AHEAD` and `DistanceType.PASSED` when the end of the railway crossing is passed.

  <a href="sdk-for-ios-navigate-protocols-railwaycrossingwarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RailwayCrossingWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18RoadClassificationO"></span>` `<span id="//apple_ref/swift/Enum/RoadClassification" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk18RoadClassificationO" class="token"><code>RoadClassification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Classification of the surrounding road environment. Note: This enum is in beta; its underlying layout is not stable and may change without any deprecation process.

  <a href="sdk-for-ios-navigate-enums-roadclassification" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RoadClassification : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8RoadSignV"></span>` `<span id="//apple_ref/swift/Struct/RoadSign" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk8RoadSignV" class="token"><code>RoadSign</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a road sign.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-roadsign" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RoadSign : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16RoadSignCategoryO"></span>` `<span id="//apple_ref/swift/Enum/RoadSignCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk16RoadSignCategoryO" class="token"><code>RoadSignCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road sign category defining a general purpose of the sign.

  <a href="sdk-for-ios-navigate-enums-roadsigncategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RoadSignCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RoadSignTypeO"></span>` `<span id="//apple_ref/swift/Enum/RoadSignType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk12RoadSignTypeO" class="token"><code>RoadSignType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A road sign type classifying road signs that can appear along a road. Some signs are standardized and look the same in all countries, e.g. <a href="sdk-for-ios-navigate-enums-roadsigntype#/s:7heresdk12RoadSignTypeO04stopC0yA2CmF">`RoadSignType.stopSign`</a>. In general, the visual appearance of the road signs can differ across countries. Some road signs can be combined with other signs, like <a href="sdk-for-ios-navigate-enums-weathertype">`WeatherType`</a> signs. The road sign will be always shown topmost.

  <a href="sdk-for-ios-navigate-enums-roadsigntype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RoadSignType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV"></span>` `<span id="//apple_ref/swift/Struct/RoadSignWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk15RoadSignWarningV" class="token"><code>RoadSignWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A road sign. The main field describing the sign is <a href="sdk-for-ios-navigate-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">`RoadSignWarning.type`</a>. Some road types are standardized, others can be country specific. A valid road sign contains known <a href="sdk-for-ios-navigate-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">`RoadSignWarning.type`</a> or <a href="sdk-for-ios-navigate-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp">`RoadSignWarning.category`</a>. Use `RoadSignWarningListener` to get notifications with current road signs.

  <a href="sdk-for-ios-navigate-structs-roadsignwarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RoadSignWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23RoadSignWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RoadSignWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk23RoadSignWarningDelegateP" class="token"><code>RoadSignWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive road sign warnings. **Note:** The road sign warner is a point warner, which means that for a road sign there will *always* be 2 warnings emitted, with the \[RoadSignWarning.distance_type\] set to <a href="sdk-for-ios-navigate-enums-distancetype#/s:7heresdk12DistanceTypeO5aheadyA2CmF">`DistanceType.ahead`</a> and <a href="sdk-for-ios-navigate-enums-distancetype#/s:7heresdk12DistanceTypeO6passedyA2CmF">`DistanceType.passed`</a> which is given when the location of the road sign is reached. A <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> 120 meters and <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> 160 meters ahead, the first \[RoadSignWarning.distance_to_road_sign_in_meters\] is 120 meters and the next \[RoadSignWarning.distance_to_road_sign_in_meters\] is then 40 meters, since that is the distance between the first and second warnings.

  <a href="sdk-for-ios-navigate-protocols-roadsignwarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RoadSignWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RoadSignWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/RoadSignWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk22RoadSignWarningOptionsV" class="token"><code>RoadSignWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides road sign warning options. Set the options for filtering of road sign notifications.

  <a href="sdk-for-ios-navigate-structs-roadsignwarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RoadSignWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19RoadSignVehicleTypeO"></span>` `<span id="//apple_ref/swift/Enum/RoadSignVehicleType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19RoadSignVehicleTypeO" class="token"><code>RoadSignVehicleType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle type for which a road sign is applicable.

  <a href="sdk-for-ios-navigate-enums-roadsignvehicletype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RoadSignVehicleType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17RoadTextsDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RoadTextsDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17RoadTextsDelegateP" class="token"><code>RoadTextsDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive textual attributes of the current road.

  <a href="sdk-for-ios-navigate-protocols-roadtextsdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RoadTextsDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RouteDeviationV"></span>` `<span id="//apple_ref/swift/Struct/RouteDeviation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk14RouteDeviationV" class="token"><code>RouteDeviation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains all the relevant information on a deviation from the route.

  <a href="sdk-for-ios-navigate-structs-routedeviation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RouteDeviation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RouteDeviationDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RouteDeviationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk22RouteDeviationDelegateP" class="token"><code>RouteDeviationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about route deviations from <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>.

  <a href="sdk-for-ios-navigate-protocols-routedeviationdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RouteDeviationDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RouteMatchedLocationV"></span>` `<span id="//apple_ref/swift/Struct/RouteMatchedLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20RouteMatchedLocationV" class="token"><code>RouteMatchedLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a location matched to a specific position on a navigation route.

  <a href="sdk-for-ios-navigate-structs-routematchedlocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RouteMatchedLocation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13RouteProgressV"></span>` `<span id="//apple_ref/swift/Struct/RouteProgress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk13RouteProgressV" class="token"><code>RouteProgress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains all the relevant information on the user’s progress along a route.

  <a href="sdk-for-ios-navigate-structs-routeprogress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RouteProgress : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19RouteProgressColorsV"></span>` `<span id="//apple_ref/swift/Struct/RouteProgressColors" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19RouteProgressColorsV" class="token"><code>RouteProgressColors</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This struct contains colors for the route progress visualization.

  <a href="sdk-for-ios-navigate-structs-routeprogresscolors" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RouteProgressColors
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21RouteProgressDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RouteProgressDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21RouteProgressDelegateP" class="token"><code>RouteProgressDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about the route progress from <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>.

  <a href="sdk-for-ios-navigate-protocols-routeprogressdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RouteProgressDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SafetyCameraTypeO"></span>` `<span id="//apple_ref/swift/Enum/SafetyCameraType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk16SafetyCameraTypeO" class="token"><code>SafetyCameraType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the type of the safety camera.

  <a href="sdk-for-ios-navigate-enums-safetycameratype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum SafetyCameraType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19SafetyCameraWarningV"></span>` `<span id="//apple_ref/swift/Struct/SafetyCameraWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19SafetyCameraWarningV" class="token"><code>SafetyCameraWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides safety camera warning information.

  <a href="sdk-for-ios-navigate-structs-safetycamerawarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SafetyCameraWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27SafetyCameraWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/SafetyCameraWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27SafetyCameraWarningDelegateP" class="token"><code>SafetyCameraWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications on safety cameras. A <a href="sdk-for-ios-navigate-structs-safetycamerawarning">`SafetyCameraWarning`</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-ios-navigate-structs-safetycamerawarning">`SafetyCameraWarning`</a> 120 meters and <a href="sdk-for-ios-navigate-structs-safetycamerawarning">`SafetyCameraWarning`</a> 160 meters ahead, the first `SafetyCameraWarning.distance_to_camera_in_meters` is 120 meters and the next `SafetyCameraWarning.distance_to_camera_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

  When `SafetyCameraWarningListener` is enabled, a new set of text notifications (e.g. “Speed camera ahead”) will be trigger if any has been also enabled. The updates for the same safety camera appear in order of the initial `DistanceType.AHEAD` event. That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.

  <a href="sdk-for-ios-navigate-protocols-safetycamerawarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol SafetyCameraWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26SafetyCameraWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SafetyCameraWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26SafetyCameraWarningOptionsV" class="token"><code>SafetyCameraWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Safety camera warning options. Set the options in order to enable them.

  <a href="sdk-for-ios-navigate-structs-safetycamerawarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SafetyCameraWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17SchoolZoneWarningV"></span>` `<span id="//apple_ref/swift/Struct/SchoolZoneWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17SchoolZoneWarningV" class="token"><code>SchoolZoneWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A school zone warning which notifies about a school zone presence on road with a speed limit different than the default speed limit applicable for cars. Use `SchoolZoneWarningListener` to get notifications about school zones.

  <a href="sdk-for-ios-navigate-structs-schoolzonewarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SchoolZoneWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25SchoolZoneWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/SchoolZoneWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk25SchoolZoneWarningDelegateP" class="token"><code>SchoolZoneWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive school zone warnings.

  <a href="sdk-for-ios-navigate-protocols-schoolzonewarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol SchoolZoneWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24SchoolZoneWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SchoolZoneWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24SchoolZoneWarningOptionsV" class="token"><code>SchoolZoneWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  School zone warning options. Set the options for configuring of school zone notifications.

  <a href="sdk-for-ios-navigate-structs-schoolzonewarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SchoolZoneWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)SDKNavigationInitializer"></span>` `<span id="//apple_ref/swift/Class/SDKNavigationInitializer" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/c:@M@heresdk@objc(cs)SDKNavigationInitializer" class="token"><code>SDKNavigationInitializer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Do not use this. This class is used to initialize internals of the SDK.

  <a href="sdk-for-ios-navigate-classes-sdknavigationinitializer" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKNavigationInitializer : NSObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15SectionProgressV"></span>` `<span id="//apple_ref/swift/Struct/SectionProgress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk15SectionProgressV" class="token"><code>SectionProgress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates a user’s progress along a <a href="sdk-for-ios-navigate-classes-section">`Section`</a>.

  <a href="sdk-for-ios-navigate-structs-sectionprogress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SectionProgress : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22SpatialAudioCuePanningC"></span>` `<span id="//apple_ref/swift/Class/SpatialAudioCuePanning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk22SpatialAudioCuePanningC" class="token"><code>SpatialAudioCuePanning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use the `SpatialAudioCuePanning` to notify each of the azimuths which compose a spatial audio trajectory along the audio cue.

  <a href="sdk-for-ios-navigate-classes-spatialaudiocuepanning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SpatialAudioCuePanning
  ```

  ``` highlight
  extension SpatialAudioCuePanning: NativeBase
  ```

  ``` highlight
  extension SpatialAudioCuePanning: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26SpatialNotificationDetailsV"></span>` `<span id="//apple_ref/swift/Struct/SpatialNotificationDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26SpatialNotificationDetailsV" class="token"><code>SpatialNotificationDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides all the information for a spatial text notification, including the maneuver data and extra data which is required to set the direction of spatialization of the audio cue.

  <a href="sdk-for-ios-navigate-structs-spatialnotificationdetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpatialNotificationDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21SpatialTrajectoryDataV"></span>` `<span id="//apple_ref/swift/Struct/SpatialTrajectoryData" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21SpatialTrajectoryDataV" class="token"><code>SpatialTrajectoryData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This struct provides all the information regarding an angular panning element, including the panning angle and whether or not it is the last element on the spatial audio trajectory.

  <a href="sdk-for-ios-navigate-structs-spatialtrajectorydata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpatialTrajectoryData : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24SpeedBasedCameraBehaviorC"></span>` `<span id="//apple_ref/swift/Class/SpeedBasedCameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk24SpeedBasedCameraBehaviorC" class="token"><code>SpeedBasedCameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use this class to follow the current location of the user, zooming in and out and changing camera tilt according to the current speed.

  <a href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SpeedBasedCameraBehavior : CameraBehavior
  ```

  ``` highlight
  extension SpeedBasedCameraBehavior: NativeBase
  ```

  ``` highlight
  extension SpeedBasedCameraBehavior: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SpeedLimitV"></span>` `<span id="//apple_ref/swift/Struct/SpeedLimit" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk10SpeedLimitV" class="token"><code>SpeedLimit</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the speed limit of the current road. Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits, the HERE SDK internally reads the current device time and notifies only on speed limits that are currently active.

  It is recommended to use

      SpeedLimit.effectiveSpeedLimitInMetersPerSecond(...)

  when an application does not offer dedicated speed limit indicators for other cases, such as weather-dependent speed limits.
  </p>

  <a href="sdk-for-ios-navigate-structs-speedlimit" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpeedLimit : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18SpeedLimitDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/SpeedLimitDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk18SpeedLimitDelegateP" class="token"><code>SpeedLimitDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive the speed limit of the current road.

  <a href="sdk-for-ios-navigate-protocols-speedlimitdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol SpeedLimitDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpeedLimitOffsetV"></span>` `<span id="//apple_ref/swift/Struct/SpeedLimitOffset" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk16SpeedLimitOffsetV" class="token"><code>SpeedLimitOffset</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that represents two separate speed limit offsets for higher and lower speed limits. A driver will be notified when the current driving speed is above the speed limit + offset. Only one of the two offsets is used depending on the current speed limit.

  <a href="sdk-for-ios-navigate-structs-speedlimitoffset" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpeedLimitOffset : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20SpeedWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/SpeedWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20SpeedWarningDelegateP" class="token"><code>SpeedWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

  **Note:** The warnings issued by this protocol don’t take into account any temporary special speed limits. See `SpeedLimitListener`.

  <a href="sdk-for-ios-navigate-protocols-speedwarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol SpeedWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19SpeedWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SpeedWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19SpeedWarningOptionsV" class="token"><code>SpeedWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that contains all options to be used for the speed limit warnings.

  <a href="sdk-for-ios-navigate-structs-speedwarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpeedWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18SpeedWarningStatusO"></span>` `<span id="//apple_ref/swift/Enum/SpeedWarningStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk18SpeedWarningStatusO" class="token"><code>SpeedWarningStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents the status of the speed warning feature.

  <a href="sdk-for-ios-navigate-enums-speedwarningstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum SpeedWarningStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20TextNotificationTypeO"></span>` `<span id="//apple_ref/swift/Enum/TextNotificationType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20TextNotificationTypeO" class="token"><code>TextNotificationType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Different types of text notifications.

  <a href="sdk-for-ios-navigate-enums-textnotificationtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TextNotificationType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TimingProfileO"></span>` `<span id="//apple_ref/swift/Enum/TimingProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk13TimingProfileO" class="token"><code>TimingProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies the timing profile used for emitting notifications and warnings.

  <a href="sdk-for-ios-navigate-enums-timingprofile" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TimingProfile : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9TollBoothV"></span>` `<span id="//apple_ref/swift/Struct/TollBooth" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk9TollBoothV" class="token"><code>TollBooth</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information of a toll stop. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-tollbooth" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollBooth : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13TollBoothLaneV"></span>` `<span id="//apple_ref/swift/Struct/TollBoothLane" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk13TollBoothLaneV" class="token"><code>TollBoothLane</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a toll booth.

  <a href="sdk-for-ios-navigate-structs-tollboothlane" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollBoothLane : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20TollCollectionMethodO"></span>` `<span id="//apple_ref/swift/Enum/TollCollectionMethod" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20TollCollectionMethodO" class="token"><code>TollCollectionMethod</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Available payment methods.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-tollcollectionmethod" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TollCollectionMethod : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TollStopV"></span>` `<span id="//apple_ref/swift/Struct/TollStop" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk8TollStopV" class="token"><code>TollStop</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides information for a toll stop with multiple toll booths.

  <a href="sdk-for-ios-navigate-structs-tollstop" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TollStop : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TollStopWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TollStopWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk23TollStopWarningDelegateP" class="token"><code>TollStopWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive information on the upcoming toll booth structure.

  The warner might also warn about gates/checkpoints for vignette, border checkpoints and similar structures on the street.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. A <a href="sdk-for-ios-navigate-structs-tollstop">`TollStop`</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-ios-navigate-structs-tollstop">`TollStop`</a> 120 meters and <a href="sdk-for-ios-navigate-structs-tollstop">`TollStop`</a> 160 meters ahead, the first `TollStop.distance_to_toll_stop_in_meters` is 120 meters and the next `TollStop.distance_to_toll_stop_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

  <a href="sdk-for-ios-navigate-protocols-tollstopwarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TollStopWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TrackingCameraBehaviorC"></span>` `<span id="//apple_ref/swift/Class/TrackingCameraBehavior" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk22TrackingCameraBehaviorC" class="token"><code>TrackingCameraBehavior</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use this class to follow a moving target. The camera smoothly tracks the target’s position while adjusting heading, tilt, and zoom as needed. When tracking starts or resumes, the camera first animates a re-centering transition to align with the target.

  Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrackingCameraBehavior : CameraBehavior
  ```

  ``` highlight
  extension TrackingCameraBehavior: NativeBase
  ```

  ``` highlight
  extension TrackingCameraBehavior: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20TrafficMergeRoadTypeO"></span>` `<span id="//apple_ref/swift/Enum/TrafficMergeRoadType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20TrafficMergeRoadTypeO" class="token"><code>TrafficMergeRoadType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of road which is merging onto the current road.

  <a href="sdk-for-ios-navigate-enums-trafficmergeroadtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficMergeRoadType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TrafficMergeSideO"></span>` `<span id="//apple_ref/swift/Enum/TrafficMergeSide" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk16TrafficMergeSideO" class="token"><code>TrafficMergeSide</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The side from where the merging traffic is joining with the current highway.

  <a href="sdk-for-ios-navigate-enums-trafficmergeside" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficMergeSide : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19TrafficMergeWarningV"></span>` `<span id="//apple_ref/swift/Struct/TrafficMergeWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk19TrafficMergeWarningV" class="token"><code>TrafficMergeWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides warning for merging traffic. The main field describing the merging traffic is `TrafficMergeWarning.road_type` specifying the type of road containing traffic which is merging with the current road. Use `TrafficMergeWarningListener` to get notifications about upcoming merging traffic.

  <a href="sdk-for-ios-navigate-structs-trafficmergewarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficMergeWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27TrafficMergeWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TrafficMergeWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk27TrafficMergeWarningDelegateP" class="token"><code>TrafficMergeWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive traffic merge warnings. **Note:** The traffic merge warner is a point warner, which means that for a traffic merge there will *always* be 2 warnings emitted, with the `TrafficMergeWarning.distance_type` set to `DistanceType.AHEAD` and `DistanceType.PASSED` which is given when the location of the traffic merge is reached. A <a href="sdk-for-ios-navigate-structs-trafficmergewarning">`TrafficMergeWarning`</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-ios-navigate-structs-trafficmergewarning">`TrafficMergeWarning`</a> 120 meters and <a href="sdk-for-ios-navigate-structs-trafficmergewarning">`TrafficMergeWarning`</a> 160 meters ahead, the first `TrafficMergeWarning.distance_to_traffic_merge_in_meters` is 120 meters and the next `TrafficMergeWarning.distance_to_traffic_merge_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

  <a href="sdk-for-ios-navigate-protocols-trafficmergewarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TrafficMergeWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26TrafficMergeWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/TrafficMergeWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk26TrafficMergeWarningOptionsV" class="token"><code>TrafficMergeWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct that provides traffic merge warning options. Set the options for filtering the traffic merge notifications.

  <a href="sdk-for-ios-navigate-structs-trafficmergewarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficMergeWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20TrafficOnRouteColorsV"></span>` `<span id="//apple_ref/swift/Struct/TrafficOnRouteColors" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk20TrafficOnRouteColorsV" class="token"><code>TrafficOnRouteColors</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This type contains colors used for the traffic with jam factor greater or equal to 4.0 on route ahead of the current location visualization.

  <a href="sdk-for-ios-navigate-structs-trafficonroutecolors" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficOnRouteColors : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV"></span>` `<span id="//apple_ref/swift/Struct/TruckRestrictionWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk23TruckRestrictionWarningV" class="token"><code>TruckRestrictionWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck or there can be a road ahead where the truck’s weight exceeds the permissible limit.

  <a href="sdk-for-ios-navigate-structs-truckrestrictionwarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TruckRestrictionWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk32TruckRestrictionsWarningDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TruckRestrictionsWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk32TruckRestrictionsWarningDelegateP" class="token"><code>TruckRestrictionsWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive truck restriction warnings.

  <a href="sdk-for-ios-navigate-protocols-truckrestrictionswarningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TruckRestrictionsWarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31TruckRestrictionsWarningOptionsV"></span>` `<span id="//apple_ref/swift/Struct/TruckRestrictionsWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk31TruckRestrictionsWarningOptionsV" class="token"><code>TruckRestrictionsWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck restrictions warning options.

  <a href="sdk-for-ios-navigate-structs-truckrestrictionswarningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TruckRestrictionsWarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15VisualNavigatorC"></span>` `<span id="//apple_ref/swift/Class/VisualNavigator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk15VisualNavigatorC" class="token"><code>VisualNavigator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides all functionality of <a href="sdk-for-ios-navigate-protocols-navigatorprotocol">`NavigatorProtocol`</a>. In addition, it provides advanced rendering capabilities for a smooth navigation experience. This includes interpolation of location updates along a route during turn-by-turn navigation and during tracking mode. By default, suitable map view settings are automatically applied. For example, a predefined current location marker is rendered. Similar to <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>, this class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-ios-navigate-protocols-locationdelegate">`LocationDelegate`</a>. Note that the VisualNavigator takes control of the MapView’s (maximum) frame rate when rendering, i.e., between

      VisualNavigator.startRendering(...)

  and
      VisualNavigator.stopRendering(...)

  calls. It overwrites the MapView’s frame rate when some camera behavior is set using the <a href="sdk-for-ios-navigate-classes-visualnavigator#/s:7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp">`VisualNavigator.guidanceFrameRate`</a>. When no camera behavior is preset, the original MapView’s frame rate (the value prior to the
      VisualNavigator.startRendering(...)

  call) will be used. While the VisualNavigator is rendering, direct changes in the MapView’s frame rate can lead to unexpected behavior and therefore should be avoided.
  </p>

  <a href="sdk-for-ios-navigate-classes-visualnavigator" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VisualNavigator : NavigatorProtocol
  ```

  ``` highlight
  extension VisualNavigator: NativeBase
  ```

  ``` highlight
  extension VisualNavigator: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21VisualNavigatorColorsC"></span>` `<span id="//apple_ref/swift/Class/VisualNavigatorColors" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21VisualNavigatorColorsC" class="token"><code>VisualNavigatorColors</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class contains colors used by <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a> to render the route and the maneuver arrow visualization.

  <a href="sdk-for-ios-navigate-classes-visualnavigatorcolors" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VisualNavigatorColors
  ```

  ``` highlight
  extension VisualNavigatorColors: NativeBase
  ```

  ``` highlight
  extension VisualNavigatorColors: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9WallClockP"></span>` `<span id="//apple_ref/swift/Protocol/WallClock" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk9WallClockP" class="token"><code>WallClock</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Clock used to properly retrieve time-dependent data from the map.

  <a href="sdk-for-ios-navigate-protocols-wallclock" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol WallClock : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28WarningNotificationDistancesV"></span>` `<span id="//apple_ref/swift/Struct/WarningNotificationDistances" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk28WarningNotificationDistancesV" class="token"><code>WarningNotificationDistances</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distances for emitting warnings according to the timing profile.

  <a href="sdk-for-ios-navigate-structs-warningnotificationdistances" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WarningNotificationDistances : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11WarningTypeO"></span>` `<span id="//apple_ref/swift/Enum/WarningType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk11WarningTypeO" class="token"><code>WarningType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies the warning type.

  <a href="sdk-for-ios-navigate-enums-warningtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum WarningType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11WeatherTypeO"></span>` `<span id="//apple_ref/swift/Enum/WeatherType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk11WeatherTypeO" class="token"><code>WeatherType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Weather type attached to <a href="sdk-for-ios-navigate-structs-roadsignwarning">`RoadSignWarning`</a> or `VehicleRestriction.Condition` which limits the conditions for which the sign is applicable.

  <a href="sdk-for-ios-navigate-enums-weathertype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum WeatherType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17WeightRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/WeightRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk17WeightRestrictionV" class="token"><code>WeightRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a weight restriction.

  <a href="sdk-for-ios-navigate-structs-weightrestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WeightRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21WeightRestrictionTypeO"></span>` `<span id="//apple_ref/swift/Enum/WeightRestrictionType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-navigation#/s:7heresdk21WeightRestrictionTypeO" class="token"><code>WeightRestrictionType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the type of a weight restriction.

  <a href="sdk-for-ios-navigate-enums-weightrestrictiontype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum WeightRestrictionType : UInt32, CaseIterable, Codable
  ```

  </div>

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

