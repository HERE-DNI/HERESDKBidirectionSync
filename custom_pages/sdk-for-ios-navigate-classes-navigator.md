---
title: "Navigator Class Reference"
slug: "sdk-for-ios-navigate-classes-navigator"
---

# Navigator

<div class="declaration">

<div class="language">

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

This class provides the basic navigation functionality. It provides notifications about current map-matched location updates (see <a href="sdk-for-ios-navigate-structs-navigablelocation">`NavigableLocation`</a>). And, if a route has been set, about the route progress (see <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a>), route deviations (see <a href="sdk-for-ios-navigate-structs-routedeviation">`RouteDeviation`</a>) and maneuver notifications (see <a href="sdk-for-ios-navigate-protocols-eventtextdelegate">`EventTextDelegate`</a>).

All transport modes are supported for turn-by-turn navigation, except for public transit. Public transit routes may lead to unsafe and unexpected results.

Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and turn-by-turn bus instructions may not be as appropriate as expected.

The <a href="sdk-for-ios-navigate-enums-transportmode">`TransportMode`</a> is determined from the provided <a href="sdk-for-ios-navigate-classes-route">`Route`</a> instance, but the actual <a href="sdk-for-ios-navigate-enums-sectiontransportmode">`SectionTransportMode`</a> can vary along a route, for example, when a ferry must be taken. When no route is set, the <a href="sdk-for-ios-navigate-structs-navigablelocation">`NavigableLocation`</a> assumes a drive scenario.

This class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-ios-navigate-protocols-locationdelegate">`LocationDelegate`</a>. The accuracy of the positioning increases with the update frequency. At least one update per second should be provided. More information can be found at `LocationAccuracy.NAVIGATION`.

**Note:** Even without provided locations, for example, while driving through a tunnel, this class can interpolate missing location events and still send <a href="sdk-for-ios-navigate-structs-navigablelocation">`NavigableLocation`</a>, <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a> and maneuver notifications.

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

  ` `<span id="/s:7heresdk9NavigatorC5routeAA5RouteCSgvp"></span>` `<span id="//apple_ref/swift/Property/route" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC5routeAA5RouteCSgvp" class="token"><code>route</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="sdk-for-ios-navigate-protocols-navigablelocationdelegate">`NavigableLocationDelegate`</a>. If set, both route progress (<a href="sdk-for-ios-navigate-protocols-routeprogressdelegate">`RouteProgressDelegate`</a>) and route deviation (<a href="sdk-for-ios-navigate-protocols-routedeviationdelegate">`RouteDeviationDelegate`</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var route: Route? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC24trackingTransportProfileAA0dE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/trackingTransportProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC24trackingTransportProfileAA0dE0VSgvp" class="token"><code>trackingTransportProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-ios-navigate-structs-transportprofile">`TransportProfile`</a> can be defined with a <a href="sdk-for-ios-navigate-structs-vehicleprofile">`VehicleProfile`</a>. A vehicle profile can have several parameters such as <a href="sdk-for-ios-navigate-enums-vehicletype">`VehicleType`</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-ios-navigate-enums-vehicletype#/s:7heresdk11VehicleTypeO3caryA2CmF">`VehicleType.car`</a> profile.

  Currently used members of <a href="sdk-for-ios-navigate-structs-transportprofile">`TransportProfile`</a>

  - <a href="sdk-for-ios-navigate-enums-vehicletype">`VehicleType`</a>: Sets the transport mode.
  - From `vehicleProfile`:
    - `grossWeightInKilograms`: Required for truck related speed information.
    - `heightInCentimeters`: Required for truck related speed information.
    - `widthInCentimeters`: Additional truck definition for more specific truck speed information.
    - `lengthInCentimeters`: Additional truck definition for more specific truck speed information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.") public var trackingTransportProfile : TransportProfile ? { get set }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC30trackingTransportSpecificationAA0dE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/trackingTransportSpecification" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC30trackingTransportSpecificationAA0dE0VSgvp" class="token"><code>trackingTransportSpecification</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the transport specification for the `Navigator`, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-ios-navigate-structs-transportspecification">`TransportSpecification`</a> must have the <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a> defined in <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-ios-navigate-structs-transportspecification">`TransportSpecification`</a> will have the transport mode set to <a href="sdk-for-ios-navigate-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.

  Currently used members of <a href="sdk-for-ios-navigate-structs-transportspecification">`TransportSpecification`</a>

  - <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a>: Sets the transport mode.
  - From <a href="sdk-for-ios-navigate-structs-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a>:
    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>: Required for truck related speed information.
    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a>: Required for truck related speed information.
    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a>: Additional truck definition for more specific truck speed information.
    - <a href="sdk-for-ios-navigate-structs-vehiclespecification#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a>: Additional truck definition for more specific truck speed information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trackingTransportSpecification: TransportSpecification? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC25navigableLocationDelegateAA09NavigabledE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/navigableLocationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC25navigableLocationDelegateAA09NavigabledE0_pSgvp" class="token"><code>navigableLocationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the current location. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var navigableLocationDelegate: NavigableLocationDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC21routeProgressDelegateAA05RoutedE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/routeProgressDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC21routeProgressDelegateAA05RoutedE0_pSgvp" class="token"><code>routeProgressDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var routeProgressDelegate: RouteProgressDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC22routeDeviationDelegateAA05RoutedE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/routeDeviationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC22routeDeviationDelegateAA05RoutedE0_pSgvp" class="token"><code>routeDeviationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var routeDeviationDelegate: RouteDeviationDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC17eventTextDelegateAA05EventdE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/eventTextDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC17eventTextDelegateAA05EventdE0_pSgvp" class="token"><code>eventTextDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive text notifications when they are available. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user. **Note:** In order to receive the text notification emitted for the traffic merge warner, when `TrafficMergeWarningOptions.enable_text_notification` has been enabled, the `sdk.navigation.EventTextListener` must be enabled as well.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var eventTextDelegate: EventTextDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC23milestoneStatusDelegateAA09MilestonedE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/milestoneStatusDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC23milestoneStatusDelegateAA09MilestonedE0_pSgvp" class="token"><code>milestoneStatusDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the arrival at each <a href="sdk-for-ios-navigate-structs-milestone">`Milestone`</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-ios-navigate-enums-milestonetype#/s:7heresdk13MilestoneTypeO8stopoveryA2CmF">`MilestoneType.stopover`</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-ios-navigate-enums-milestonetype#/s:7heresdk13MilestoneTypeO11passthroughyA2CmF">`MilestoneType.passthrough`</a> are excluded, by default, but can be included via <a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC37isPassthroughWaypointsHandlingEnabledSbvp">`isPassthroughWaypointsHandlingEnabled`</a>. Milestone status notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var milestoneStatusDelegate: MilestoneStatusDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC26destinationReachedDelegateAA011DestinationdE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/destinationReachedDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC26destinationReachedDelegateAA011DestinationdE0_pSgvp" class="token"><code>destinationReachedDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var destinationReachedDelegate: DestinationReachedDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC20speedWarningDelegateAA05SpeeddE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/speedWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC20speedWarningDelegateAA05SpeeddE0_pSgvp" class="token"><code>speedWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var speedWarningDelegate: SpeedWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverdefG0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/maneuverViewLaneAssistanceDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverdefG0_pSgvp" class="token"><code>maneuverViewLaneAssistanceDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var maneuverViewLaneAssistanceDelegate: ManeuverViewLaneAssistanceDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentdefgH0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/currentSituationLaneAssistanceViewDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentdefgH0_pSgvp" class="token"><code>currentSituationLaneAssistanceViewDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive current situation lane assistance view notifications. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var currentSituationLaneAssistanceViewDelegate: CurrentSituationLaneAssistanceViewDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentaldeG0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/environmentalZoneWarningListenerDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentaldeG0_pSgvp" class="token"><code>environmentalZoneWarningListenerDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notification on approaching environmental zones. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var environmentalZoneWarningListenerDelegate: EnvironmentalZoneWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC34junctionViewLaneAssistanceDelegateAA08JunctiondefG0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/junctionViewLaneAssistanceDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC34junctionViewLaneAssistanceDelegateAA08JunctiondefG0_pSgvp" class="token"><code>junctionViewLaneAssistanceDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var junctionViewLaneAssistanceDelegate: JunctionViewLaneAssistanceDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC27safetyCameraWarningDelegateAA06SafetydeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/safetyCameraWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC27safetyCameraWarningDelegateAA06SafetydeF0_pSgvp" class="token"><code>safetyCameraWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive safety camera warner notifications. If a delegate delegate is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-ios-navigate-protocols-safetycamerawarningdelegate">`SafetyCameraWarningDelegate`</a>. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var safetyCameraWarningDelegate: SafetyCameraWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC26safetyCameraWarningOptionsAA06SafetydeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/safetyCameraWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC26safetyCameraWarningOptionsAA06SafetydeF0Vvp" class="token"><code>safetyCameraWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Safety camera warning options to be passed to <a href="sdk-for-ios-navigate-protocols-safetycamerawarningdelegate">`SafetyCameraWarningDelegate`</a>. These options allow the enabling or disabling the text notification for the warner.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var safetyCameraWarningOptions: SafetyCameraWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC33dangerZoneWarningListenerDelegateAA06DangerdeG0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/dangerZoneWarningListenerDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC33dangerZoneWarningListenerDelegateAA06DangerdeG0_pSgvp" class="token"><code>dangerZoneWarningListenerDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notification on approaching danger zones. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var dangerZoneWarningListenerDelegate: DangerZoneWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC32truckRestrictionsWarningDelegateAA05TruckdeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/truckRestrictionsWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC32truckRestrictionsWarningDelegateAA05TruckdeF0_pSgvp" class="token"><code>truckRestrictionsWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about truck restrictions on the current road. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var truckRestrictionsWarningDelegate: TruckRestrictionsWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC12warnerEngineAA06WarnerD0Cvp"></span>` `<span id="//apple_ref/swift/Property/warnerEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC12warnerEngineAA06WarnerD0Cvp" class="token"><code>warnerEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Warner engine used by the navigator. This engine can be used to configure navigation warnings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var warnerEngine: WarnerEngine { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC31truckRestrictionsWarningOptionsAA05TruckdeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/truckRestrictionsWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC31truckRestrictionsWarningOptionsAA05TruckdeF0Vvp" class="token"><code>truckRestrictionsWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-ios-navigate-protocols-truckrestrictionswarningdelegate">`TruckRestrictionsWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckRestrictionsWarningOptions: TruckRestrictionsWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC18postActionDelegateAA04PostdE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/postActionDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC18postActionDelegateAA04PostdE0_pSgvp" class="token"><code>postActionDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var postActionDelegate: PostActionDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC18speedLimitDelegateAA05SpeeddE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/speedLimitDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC18speedLimitDelegateAA05SpeeddE0_pSgvp" class="token"><code>speedLimitDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the speed limit of the current road. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var speedLimitDelegate: SpeedLimitDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC17roadTextsDelegateAA04RoaddE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/roadTextsDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC17roadTextsDelegateAA04RoaddE0_pSgvp" class="token"><code>roadTextsDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the textual attributes of the current road. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var roadTextsDelegate: RoadTextsDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC22roadAttributesDelegateAA04RoaddE0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/roadAttributesDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC22roadAttributesDelegateAA04RoaddE0_pSgvp" class="token"><code>roadAttributesDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about attributes of the current road. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var roadAttributesDelegate: RoadAttributesDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC23roadSignWarningDelegateAA04RoaddeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/roadSignWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC23roadSignWarningDelegateAA04RoaddeF0_pSgvp" class="token"><code>roadSignWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about road signs on the current road. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var roadSignWarningDelegate: RoadSignWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC22roadSignWarningOptionsAA04RoaddeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/roadSignWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC22roadSignWarningOptionsAA04RoaddeF0Vvp" class="token"><code>roadSignWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-ios-navigate-protocols-roadsignwarningdelegate">`RoadSignWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadSignWarningOptions: RoadSignWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC25schoolZoneWarningDelegateAA06SchooldeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/schoolZoneWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC25schoolZoneWarningDelegateAA06SchooldeF0_pSgvp" class="token"><code>schoolZoneWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about school zones on the current road. Setting `nil` value to the delegate will unset the delegate. school zones on the current road. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var schoolZoneWarningDelegate: SchoolZoneWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC24schoolZoneWarningOptionsAA06SchooldeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/schoolZoneWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC24schoolZoneWarningOptionsAA06SchooldeF0Vvp" class="token"><code>schoolZoneWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  School zone warning options It allow to configure school zone notifications to be passed to <a href="sdk-for-ios-navigate-protocols-schoolzonewarningdelegate">`SchoolZoneWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var schoolZoneWarningOptions: SchoolZoneWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC28realisticViewWarningDelegateAA09RealisticdeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/realisticViewWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC28realisticViewWarningDelegateAA09RealisticdeF0_pSgvp" class="token"><code>realisticViewWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about junction views on the current road. Setting `nil` value to the delegate will unset the delegate. This feature requires a map version greater or equal to 67 in order to function properly. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var realisticViewWarningDelegate: RealisticViewWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC27realisticViewWarningOptionsAA09RealisticdeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/realisticViewWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC27realisticViewWarningOptionsAA09RealisticdeF0Vvp" class="token"><code>realisticViewWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Realistic view warning options. It allow to filter realistic views to be passed to <a href="sdk-for-ios-navigate-protocols-realisticviewwarningdelegate">`RealisticViewWarningDelegate`</a>.

  - This feature requires a map version greater or equal to 67 in order to function properly.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var realisticViewWarningOptions: RealisticViewWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC29borderCrossingWarningDelegateAA06BorderdeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/borderCrossingWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC29borderCrossingWarningDelegateAA06BorderdeF0_pSgvp" class="token"><code>borderCrossingWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var borderCrossingWarningDelegate: BorderCrossingWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC28borderCrossingWarningOptionsAA06BorderdeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/borderCrossingWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC28borderCrossingWarningOptionsAA06BorderdeF0Vvp" class="token"><code>borderCrossingWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Border crossing warning options to be passed to <a href="sdk-for-ios-navigate-protocols-bordercrossingwarningdelegate">`BorderCrossingWarningDelegate`</a>. These options allow the filtering of the border crossing warnings received and set the notification distances.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var borderCrossingWarningOptions: BorderCrossingWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC23tollStopWarningDelegateAA04TolldeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/tollStopWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC23tollStopWarningDelegateAA04TolldeF0_pSgvp" class="token"><code>tollStopWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive information on the upcoming toll stop. Setting `nil` value to the delegate will unset the delegate. This is a **beta release** of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var tollStopWarningDelegate: TollStopWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC30railwayCrossingWarningDelegateAA07RailwaydeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/railwayCrossingWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC30railwayCrossingWarningDelegateAA07RailwaydeF0_pSgvp" class="token"><code>railwayCrossingWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var railwayCrossingWarningDelegate: RailwayCrossingWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC27lowSpeedZoneWarningDelegateAA03LowdefG0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/lowSpeedZoneWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC27lowSpeedZoneWarningDelegateAA03LowdefG0_pSgvp" class="token"><code>lowSpeedZoneWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This delegate is currently available *only* for Japan. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var lowSpeedZoneWarningDelegate: LowSpeedZoneWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC27trafficMergeWarningDelegateAA07TrafficdeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/trafficMergeWarningDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC27trafficMergeWarningDelegateAA07TrafficdeF0_pSgvp" class="token"><code>trafficMergeWarningDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about merging traffic to the current road. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var trafficMergeWarningDelegate: TrafficMergeWarningDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC26trafficMergeWarningOptionsAA07TrafficdeF0Vvp"></span>` `<span id="//apple_ref/swift/Property/trafficMergeWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC26trafficMergeWarningOptionsAA07TrafficdeF0Vvp" class="token"><code>trafficMergeWarningOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-ios-navigate-protocols-trafficmergewarningdelegate">`TrafficMergeWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficMergeWarningOptions: TrafficMergeWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC33offRoadDestinationReachedDelegateAA03OffdefG0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/offRoadDestinationReachedDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC33offRoadDestinationReachedDelegateAA03OffdefG0_pSgvp" class="token"><code>offRoadDestinationReachedDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offRoadDestinationReachedDelegate: OffRoadDestinationReachedDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC23offRoadProgressDelegateAA03OffdeF0_pSgvp"></span>` `<span id="//apple_ref/swift/Property/offRoadProgressDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC23offRoadProgressDelegateAA03OffdeF0_pSgvp" class="token"><code>offRoadProgressDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offRoadProgressDelegate: OffRoadProgressDelegate? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC27maneuverNotificationOptionsAA08ManeuverdE0Vvp"></span>` `<span id="//apple_ref/swift/Property/maneuverNotificationOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC27maneuverNotificationOptionsAA08ManeuverdE0Vvp" class="token"><code>maneuverNotificationOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used for maneuver notifications. Notifications are only available if a route is present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverNotificationOptions: ManeuverNotificationOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC16eventTextOptionsAA05EventdE0Vvp"></span>` `<span id="//apple_ref/swift/Property/eventTextOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC16eventTextOptionsAA05EventdE0Vvp" class="token"><code>eventTextOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used for text notifications. Notifications are only available if a route is present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var eventTextOptions: EventTextOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC19speedWarningOptionsAA05SpeeddE0Vvp"></span>` `<span id="//apple_ref/swift/Property/speedWarningOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC19speedWarningOptionsAA05SpeeddE0Vvp" class="token"><code>speedWarningOptions</code></a>` `

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
  public var speedWarningOptions: SpeedWarningOptions { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC27isEnableTunnelExtrapolationSbvp"></span>` `<span id="//apple_ref/swift/Property/isEnableTunnelExtrapolation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC27isEnableTunnelExtrapolationSbvp" class="token"><code>isEnableTunnelExtrapolation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isEnableTunnelExtrapolation: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC37isPassthroughWaypointsHandlingEnabledSbvp"></span>` `<span id="//apple_ref/swift/Property/isPassthroughWaypointsHandlingEnabled" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC37isPassthroughWaypointsHandlingEnabledSbvp" class="token"><code>isPassthroughWaypointsHandlingEnabled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPassthroughWaypointsHandlingEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC14trafficOnRouteAA07TrafficdE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/trafficOnRoute" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC14trafficOnRouteAA07TrafficdE0VSgvp" class="token"><code>trafficOnRoute</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic information for the current route. This impacts <a href="sdk-for-ios-navigate-structs-routeprogress">`RouteProgress`</a> updates as the duration of the <a href="sdk-for-ios-navigate-structs-sectionprogress">`SectionProgress`</a> might change. However, the remaining distance and the route geometry will remain unchanged.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficOnRoute: TrafficOnRoute? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9NavigatorC15locationManagerAA08LocationD0Cvp"></span>` `<span id="//apple_ref/swift/Property/locationManager" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-navigator#/s:7heresdk9NavigatorC15locationManagerAA08LocationD0Cvp" class="token"><code>locationManager</code></a>` `

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
  public var locationManager: LocationManager { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      getManeuver(index: )

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
  public func getManeuver ( index : Int32 ) -> Maneuver ?
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

      getManeuverNotificationTimingOptions(transportMode: timingProfile: )

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
  public func getManeuverNotificationTimingOptions ( transportMode : TransportMode , timingProfile : TimingProfile ) -> ManeuverNotificationTimingOptions
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

      setManeuverNotificationTimingOptions(transportMode: timingProfile: options: )

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
  @discardableResult public func setManeuverNotificationTimingOptions ( transportMode : TransportMode , timingProfile : TimingProfile , options : ManeuverNotificationTimingOptions ) -> Bool
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

  `True` if set successfully, `false` when options has invalid value, see <a href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions">`ManeuverNotificationTimingOptions`</a> for more details about options.

  </div>

  </div>

  </div>

- <div>

      getWarningNotificationDistances(warningType: )

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
  public func getWarningNotificationDistances ( warningType : WarningType ) -> WarningNotificationDistances
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

      setWarningNotificationDistances(warningType: warningNotificationDistances: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Set the warning notification distances for the specified warning types. **Note:** The warning notification distances are set for most warners. This method can’t be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use `NavigatorInterface.school_zone_warning_options` instead. Attempting to set the warning notification distances for the school zone warner using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false`. Always use `SchoolZoneWarningOptions.warning_distance_in_meters` to set the warning notification distance for the school zone warner regardless of the <a href="sdk-for-ios-navigate-enums-timingprofile">`TimingProfile`</a>. If `NavigatorInterface.set_warning_notification_distances` could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false`. Always use `TrafficMergeWarningOptions.warning_distance_in_meters` to set the warning notification distance for the traffic merge warner regardless of the <a href="sdk-for-ios-navigate-enums-timingprofile">`TimingProfile`</a>. Using the `NavigatorInterface.set_warning_notification_distances` method will fail and return `false` to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func setWarningNotificationDistances ( warningType : WarningType , warningNotificationDistances : WarningNotificationDistances ) -> Bool
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

  `True` if set successfully, `false` when the warning_type is \[WarningType.SCHOOL_ZONE\] or the options have invalid values, see <a href="sdk-for-ios-navigate-structs-warningnotificationdistances">`WarningNotificationDistances`</a> for more details about warning notification distances.

  </div>

  </div>

  </div>

- <div>

      repeatLastManeuverNotification()

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
  public func repeatLastManeuverNotification ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      calculateRemainingDistanceInMeters(coordinates: )

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
  public func calculateRemainingDistanceInMeters ( coordinates : GeoCoordinates ) -> Int32 ?
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

      setCustomOption(key: value: )

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
  public func setCustomOption ( key : String , value : String )
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

- <div>

      onLocationUpdated(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time a new location is available. In a navigation context while using the `Navigator` or <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a>, it’s required to set the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter for each <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object so that the HERE SDK can map-match the locations properly. If the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onLocationUpdated ( _ location : Location )
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

      availableLanguagesForManeuverNotifications()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the list of languages for maneuver notification currently available in the SDK.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func availableLanguagesForManeuverNotifications () -> [ LanguageCode ]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  the list of languages for maneuver notification currently available in the SDK.

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

