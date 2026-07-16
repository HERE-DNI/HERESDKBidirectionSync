---
title: "NavigatorProtocol Protocol Reference"
slug: "sdk-for-ios-explore-protocols-navigatorprotocol"
---

# NavigatorProtocol

<div class="declaration">

<div class="language">

``` highlight
public protocol NavigatorProtocol : LocationDelegate
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>

</div>

This protocol provides the basic functionality needed to run a navigation session.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP5routeAA5RouteCSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-route" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP5routeAA5RouteCSgvp" class="token"><code>route</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route to navigate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var route: Route? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-route">Route</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP24trackingTransportProfileAA0eF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trackingTransportProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP24trackingTransportProfileAA0eF0VSgvp" class="token"><code>trackingTransportProfile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the transport profile for the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a>, when no route is present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.")
  var trackingTransportProfile: TransportProfile? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-transportprofile">TransportProfile</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP30trackingTransportSpecificationAA0eF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trackingTransportSpecification" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP30trackingTransportSpecificationAA0eF0VSgvp" class="token"><code>trackingTransportSpecification</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the transport specification for the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a>, when no route is present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var trackingTransportSpecification: TransportSpecification? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP25navigableLocationDelegateAA09NavigableeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-navigableLocationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP25navigableLocationDelegateAA09NavigableeF0_pSgvp" class="token"><code>navigableLocationDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the current location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var navigableLocationDelegate: NavigableLocationDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-navigablelocationdelegate">NavigableLocationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP21routeProgressDelegateAA05RouteeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeProgressDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP21routeProgressDelegateAA05RouteeF0_pSgvp" class="token"><code>routeProgressDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about navigation route progress.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var routeProgressDelegate: RouteProgressDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-routeprogressdelegate">RouteProgressDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP22routeDeviationDelegateAA05RouteeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeDeviationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP22routeDeviationDelegateAA05RouteeF0_pSgvp" class="token"><code>routeDeviationDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about deviations from the route if any occurs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var routeDeviationDelegate: RouteDeviationDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-routedeviationdelegate">RouteDeviationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP17eventTextDelegateAA05EventeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-eventTextDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP17eventTextDelegateAA05EventeF0_pSgvp" class="token"><code>eventTextDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive text notifications when they are available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var eventTextDelegate: EventTextDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-eventtextdelegate">EventTextDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23milestoneStatusDelegateAA09MilestoneeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-milestoneStatusDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23milestoneStatusDelegateAA09MilestoneeF0_pSgvp" class="token"><code>milestoneStatusDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the arrival at each <a href="sdk-for-ios-explore-structs-milestone">`Milestone`</a> or missing it.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var milestoneStatusDelegate: MilestoneStatusDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP26destinationReachedDelegateAA011DestinationeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-destinationReachedDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP26destinationReachedDelegateAA011DestinationeF0_pSgvp" class="token"><code>destinationReachedDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive the notification about the arrival at the destination.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var destinationReachedDelegate: DestinationReachedDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-destinationreacheddelegate">DestinationReachedDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP20speedWarningDelegateAA05SpeedeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP20speedWarningDelegateAA05SpeedeF0_pSgvp" class="token"><code>speedWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var speedWarningDelegate: SpeedWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-speedwarningdelegate">SpeedWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverViewLaneAssistanceDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp" class="token"><code>maneuverViewLaneAssistanceDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive maneuver view lane assistance notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var maneuverViewLaneAssistanceDelegate: ManeuverViewLaneAssistanceDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-currentSituationLaneAssistanceViewDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp" class="token"><code>currentSituationLaneAssistanceViewDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive current situation lane assistance view notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var currentSituationLaneAssistanceViewDelegate: CurrentSituationLaneAssistanceViewDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-environmentalZoneWarningListenerDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp" class="token"><code>environmentalZoneWarningListenerDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notification on approaching environmental zones.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var environmentalZoneWarningListenerDelegate: EnvironmentalZoneWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-junctionViewLaneAssistanceDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp" class="token"><code>junctionViewLaneAssistanceDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive junction view lane assistance notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var junctionViewLaneAssistanceDelegate: JunctionViewLaneAssistanceDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-safetyCameraWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp" class="token"><code>safetyCameraWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive safety camera warner notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var safetyCameraWarningDelegate: SafetyCameraWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP26safetyCameraWarningOptionsAA06SafetyefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-safetyCameraWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP26safetyCameraWarningOptionsAA06SafetyefG0Vvp" class="token"><code>safetyCameraWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Safety camera warning options to be passed to <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">`SafetyCameraWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var safetyCameraWarningOptions: SafetyCameraWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-dangerZoneWarningListenerDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp" class="token"><code>dangerZoneWarningListenerDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notification on approaching danger zones.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var dangerZoneWarningListenerDelegate: DangerZoneWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckRestrictionsWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp" class="token"><code>truckRestrictionsWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about truck restrictions on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var truckRestrictionsWarningDelegate: TruckRestrictionsWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP12warnerEngineAA06WarnerE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-warnerEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP12warnerEngineAA06WarnerE0Cvp" class="token"><code>warnerEngine</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Warner engine used by the navigator.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var warnerEngine: WarnerEngine { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-warnerengine">WarnerEngine</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP31truckRestrictionsWarningOptionsAA05TruckefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckRestrictionsWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP31truckRestrictionsWarningOptionsAA05TruckefG0Vvp" class="token"><code>truckRestrictionsWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-ios-explore-protocols-truckrestrictionswarningdelegate">`TruckRestrictionsWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var truckRestrictionsWarningOptions: TruckRestrictionsWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP18postActionDelegateAA04PosteF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-postActionDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP18postActionDelegateAA04PosteF0_pSgvp" class="token"><code>postActionDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive post action notifications, such as a charge action at a charging station.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var postActionDelegate: PostActionDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-postactiondelegate">PostActionDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP18speedLimitDelegateAA05SpeedeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedLimitDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP18speedLimitDelegateAA05SpeedeF0_pSgvp" class="token"><code>speedLimitDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the speed limit of the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var speedLimitDelegate: SpeedLimitDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-speedlimitdelegate">SpeedLimitDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP17roadTextsDelegateAA04RoadeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadTextsDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP17roadTextsDelegateAA04RoadeF0_pSgvp" class="token"><code>roadTextsDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the textual attributes of the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var roadTextsDelegate: RoadTextsDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-roadtextsdelegate">RoadTextsDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP22roadAttributesDelegateAA04RoadeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadAttributesDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP22roadAttributesDelegateAA04RoadeF0_pSgvp" class="token"><code>roadAttributesDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about attributes of the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var roadAttributesDelegate: RoadAttributesDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-roadattributesdelegate">RoadAttributesDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23roadSignWarningDelegateAA04RoadefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadSignWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23roadSignWarningDelegateAA04RoadefG0_pSgvp" class="token"><code>roadSignWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about road signs on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var roadSignWarningDelegate: RoadSignWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP22roadSignWarningOptionsAA04RoadefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadSignWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP22roadSignWarningOptionsAA04RoadefG0Vvp" class="token"><code>roadSignWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-ios-explore-protocols-roadsignwarningdelegate">`RoadSignWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var roadSignWarningOptions: RoadSignWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-roadsignwarningoptions">RoadSignWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-schoolZoneWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp" class="token"><code>schoolZoneWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about school zones on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var schoolZoneWarningDelegate: SchoolZoneWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP24schoolZoneWarningOptionsAA06SchoolefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-schoolZoneWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP24schoolZoneWarningOptionsAA06SchoolefG0Vvp" class="token"><code>schoolZoneWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  School zone warning options

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var schoolZoneWarningOptions: SchoolZoneWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP28realisticViewWarningDelegateAA09RealisticefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-realisticViewWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP28realisticViewWarningDelegateAA09RealisticefG0_pSgvp" class="token"><code>realisticViewWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about junction views on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var realisticViewWarningDelegate: RealisticViewWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27realisticViewWarningOptionsAA09RealisticefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-realisticViewWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27realisticViewWarningOptionsAA09RealisticefG0Vvp" class="token"><code>realisticViewWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Realistic view warning options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var realisticViewWarningOptions: RealisticViewWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP29borderCrossingWarningDelegateAA06BorderefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-borderCrossingWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP29borderCrossingWarningDelegateAA06BorderefG0_pSgvp" class="token"><code>borderCrossingWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about border crossings on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var borderCrossingWarningDelegate: BorderCrossingWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP28borderCrossingWarningOptionsAA06BorderefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-borderCrossingWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP28borderCrossingWarningOptionsAA06BorderefG0Vvp" class="token"><code>borderCrossingWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Border crossing warning options to be passed to <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">`BorderCrossingWarningDelegate`</a>. These options

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var borderCrossingWarningOptions: BorderCrossingWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23tollStopWarningDelegateAA04TollefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tollStopWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23tollStopWarningDelegateAA04TollefG0_pSgvp" class="token"><code>tollStopWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive information on the upcoming toll stop.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var tollStopWarningDelegate: TollStopWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-railwayCrossingWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp" class="token"><code>railwayCrossingWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about railway crossings on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var railwayCrossingWarningDelegate: RailwayCrossingWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lowSpeedZoneWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp" class="token"><code>lowSpeedZoneWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about low speed zones on the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var lowSpeedZoneWarningDelegate: LowSpeedZoneWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficMergeWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp" class="token"><code>trafficMergeWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about merging traffic to the current road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var trafficMergeWarningDelegate: TrafficMergeWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP26trafficMergeWarningOptionsAA07TrafficefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficMergeWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP26trafficMergeWarningOptionsAA07TrafficefG0Vvp" class="token"><code>trafficMergeWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-ios-explore-protocols-trafficmergewarningdelegate">`TrafficMergeWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var trafficMergeWarningOptions: TrafficMergeWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-offRoadDestinationReachedDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp" class="token"><code>offRoadDestinationReachedDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive the notification about the arrival at the off-road destination.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var offRoadDestinationReachedDelegate: OffRoadDestinationReachedDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23offRoadProgressDelegateAA03OffefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-offRoadProgressDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP23offRoadProgressDelegateAA03OffefG0_pSgvp" class="token"><code>offRoadProgressDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive the notification about the off-road progress.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var offRoadProgressDelegate: OffRoadProgressDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27maneuverNotificationOptionsAA08ManeuvereF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverNotificationOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27maneuverNotificationOptionsAA08ManeuvereF0Vvp" class="token"><code>maneuverNotificationOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used for maneuver notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var maneuverNotificationOptions: ManeuverNotificationOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP16eventTextOptionsAA05EventeF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-eventTextOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP16eventTextOptionsAA05EventeF0Vvp" class="token"><code>eventTextOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used for text notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var eventTextOptions: EventTextOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-eventtextoptions">EventTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP19speedWarningOptionsAA05SpeedeF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP19speedWarningOptionsAA05SpeedeF0Vvp" class="token"><code>speedWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used for the speed warning feature.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var speedWarningOptions: SpeedWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-speedwarningoptions">SpeedWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27isEnableTunnelExtrapolationSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isEnableTunnelExtrapolation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP27isEnableTunnelExtrapolationSbvp" class="token"><code>isEnableTunnelExtrapolation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines whether to enable or disable tunnel extrapolation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var isEnableTunnelExtrapolation: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP37isPassthroughWaypointsHandlingEnabledSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isPassthroughWaypointsHandlingEnabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP37isPassthroughWaypointsHandlingEnabledSbvp" class="token"><code>isPassthroughWaypointsHandlingEnabled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines whether to enable or disable handling of passthrough waypoints.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var isPassthroughWaypointsHandlingEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP14trafficOnRouteAA07TrafficeF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP14trafficOnRouteAA07TrafficeF0VSgvp" class="token"><code>trafficOnRoute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic information for the current route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var trafficOnRoute: TrafficOnRoute? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficonroute">TrafficOnRoute</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP15locationManagerAA08LocationE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-locationManager" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP15locationManagerAA08LocationE0Cvp" class="token"><code>locationManager</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The location manager used by the navigator for map-matched location processing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var locationManager: LocationManager { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-locationmanager">LocationManager</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP17onLocationUpdatedyyAA0E0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onLocationUpdated-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP17onLocationUpdatedyyAA0E0VF" class="token"><code>onLocationUpdated(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time a new location is available. In a navigation context while using the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a> or <a href="sdk-for-ios-explore-classes-visualnavigator">`VisualNavigator`</a>, it’s required to set the <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object so that the HERE SDK can map-match the locations properly. If the <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onLocationUpdated(_ location: Location)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-location">Location</a>

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
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>Current location.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP11getManeuver5indexAA0E0CSgs5Int32V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getManeuver-index" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP11getManeuver5indexAA0E0CSgs5Int32V_tF" class="token"><code>getManeuver(index:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns maneuver at the given index.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getManeuver(index: Int32) -> Maneuver?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-maneuver">Maneuver</a>

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
  <td><code> </code><em><code>index</code></em><code> </code></td>
  <td><div>
  <p>The index of maneuver requested.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The maneuver if it exists or otherwise `nil`.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getManeuverNotificationTimingOptions-transportMode-timingProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF" class="token"><code>getManeuverNotificationTimingOptions(transportMode:</code><wbr></wbr><code>timingProfile:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getManeuverNotificationTimingOptions(transportMode: TransportMode, timingProfile: TimingProfile) -> ManeuverNotificationTimingOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>
  - <a href="sdk-for-ios-explore-enums-timingprofile">TimingProfile</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a>

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
  <td><code> </code><em><code>transportMode</code></em><code> </code></td>
  <td><div>
  <p>The transport mode of the timing options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>timingProfile</code></em><code> </code></td>
  <td><div>
  <p>The timing profile of the timing options.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The timing options with default values.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setManeuverNotificationTimingOptions-transportMode-timingProfile-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF" class="token"><code>setManeuverNotificationTimingOptions(transportMode:</code><wbr></wbr><code>timingProfile:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set timing option values for the combination of transport mode and timing profile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func setManeuverNotificationTimingOptions(transportMode: TransportMode, timingProfile: TimingProfile, options: ManeuverNotificationTimingOptions) -> Bool
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>
  - <a href="sdk-for-ios-explore-enums-timingprofile">TimingProfile</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a>

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
  <td><code> </code><em><code>transportMode</code></em><code> </code></td>
  <td><div>
  <p>The transport mode of the timing options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>timingProfile</code></em><code> </code></td>
  <td><div>
  <p>The timing profile of the timing options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The timing options.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `True` if set successfully, `false` when options has invalid value, see <a href="sdk-for-ios-explore-structs-maneuvernotificationtimingoptions">`ManeuverNotificationTimingOptions`</a> for more details about options.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getWarningNotificationDistances-warningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF" class="token"><code>getWarningNotificationDistances(warningType:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling `setWarningNotificationDistances` function with the same warning type and the modified warning notification distances object.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func getWarningNotificationDistances(warningType: WarningType) -> WarningNotificationDistances
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>

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
  <td><code> </code><em><code>warningType</code></em><code> </code></td>
  <td><div>
  <p>The warning type for which the notification distances will be returned.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The notification distances for the given warning type.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setWarningNotificationDistances-warningType-warningNotificationDistances" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF" class="token"><code>setWarningNotificationDistances(warningType:</code><wbr></wbr><code>warningNotificationDistances:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set the warning notification distances for the specified warning types. **Note:** The warning notification distances are set for most warners. This method can’t be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use `NavigatorInterface.school_zone_warning_options` instead. Attempting to set the warning notification distances for the school zone warner using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false`. Always use `SchoolZoneWarningOptions.warning_distance_in_meters` to set the warning notification distance for the school zone warner regardless of the <a href="sdk-for-ios-explore-enums-timingprofile">`TimingProfile`</a>. If `NavigatorInterface.set_warning_notification_distances` could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false`. Always use `TrafficMergeWarningOptions.warning_distance_in_meters` to set the warning notification distance for the traffic merge warner regardless of the <a href="sdk-for-ios-explore-enums-timingprofile">`TimingProfile`</a>. Using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false` to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  func setWarningNotificationDistances(warningType: WarningType, warningNotificationDistances: WarningNotificationDistances) -> Bool
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>

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
  <td><code> </code><em><code>warningType</code></em><code> </code></td>
  <td><div>
  <p>The warning type for which the warning notification distances will be set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>warningNotificationDistances</code></em><code> </code></td>
  <td><div>
  <p>The warning notification distances to be set for the specified warning types.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `True` if set successfully, `false` when the warning_type is \[WarningType.SCHOOL_ZONE\] or the options have invalid values, see <a href="sdk-for-ios-explore-structs-warningnotificationdistances">`WarningNotificationDistances`</a> for more details about warning notification distances.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP30repeatLastManeuverNotificationyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-repeatLastManeuverNotification" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP30repeatLastManeuverNotificationyyF" class="token"><code>repeatLastManeuverNotification()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func repeatLastManeuverNotification()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRemainingDistanceInMeters-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF" class="token"><code>calculateRemainingDistanceInMeters(coordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func calculateRemainingDistanceInMeters(coordinates: GeoCoordinates) -> Int32?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

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
  <p>The geographic coordinates of the location.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  distance in meters or null if given coordinates are not on route or given coordinates were already traversed.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP15setCustomOption3key5valueySS_SStF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCustomOption-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-navigatorprotocol#sdk-for-ios-explore-s-7heresdk17NavigatorProtocolP15setCustomOption3key5valueySS_SStF" class="token"><code>setCustomOption(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func setCustomOption(key: String, value: String)
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>Option name</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>New option value</p>
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

