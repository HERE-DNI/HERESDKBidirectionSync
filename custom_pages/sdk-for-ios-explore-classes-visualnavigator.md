---
title: "VisualNavigator Class Reference"
slug: "sdk-for-ios-explore-classes-visualnavigator"
---

# VisualNavigator

<div class="declaration">

<div class="language">

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

Related types:

- <a href="sdk-for-ios-explore-protocols-navigatorprotocol">NavigatorProtocol</a>

</div>

This class provides all functionality of <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a>. In addition, it provides advanced rendering capabilities for a smooth navigation experience. This includes interpolation of location updates along a route during turn-by-turn navigation and during tracking mode. By default, suitable map view settings are automatically applied. For example, a predefined current location marker is rendered. Similar to <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a>, this class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-ios-explore-protocols-locationdelegate">`LocationDelegate`</a>. Note that the VisualNavigator takes control of the MapView’s (maximum) frame rate when rendering, i.e., between <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">`VisualNavigator.startRendering(...)`</a> and <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC13stopRenderingyyF">`VisualNavigator.stopRendering(...)`</a> calls. It overwrites the MapView’s frame rate when some camera behavior is set using the <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp">`VisualNavigator.guidanceFrameRate`</a>. When no camera behavior is preset, the original MapView’s frame rate (the value prior to the <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">`VisualNavigator.startRendering(...)`</a> call) will be used. While the VisualNavigator is rendering, direct changes in the MapView’s frame rate can lead to unexpected behavior and therefore should be avoided.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorCACyKcfc" class="token"><code>init()</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when operation fails.

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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC9sdkEngineAcA09SDKNativeE0C_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC9sdkEngineAcA09SDKNativeE0C_tKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when operation fails.

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
  <p>An SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC9navigatorAcA0C8Protocol_p_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-navigator" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC9navigatorAcA0C8Protocol_p_tKcfc" class="token"><code>init(navigator:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class using provided instance of <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> as source of data.

  **Note:** The `VisualNavigator` implements the <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> interface and forwards all calls to the underlying <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> instance. When multiple `VisualNavigator` instances share the same <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> instance, method calls on this common instance will overwrite changes made by another, which may lead to unexpected behavior.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when operation fails.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(navigator: NavigatorProtocol) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-navigatorprotocol">NavigatorProtocol</a>

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
  <td><code> </code><em><code>navigator</code></em><code> </code></td>
  <td><div>
  <p>A NavigatorInterface implementation instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC9sdkEngine9navigatorAcA09SDKNativeE0C_AA0C8Protocol_ptKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine-navigator" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC9sdkEngine9navigatorAcA09SDKNativeE0C_AA0C8Protocol_ptKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>navigator:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class using provided instance of <a href="sdk-for-ios-explore-protocols-navigatorprotocol">`NavigatorProtocol`</a> as source of data.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when operation fails.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(sdkEngine: SDKNativeEngine, navigator: NavigatorProtocol) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-protocols-navigatorprotocol">NavigatorProtocol</a>

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
  <p>An SDKEngine instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>navigator</code></em><code> </code></td>
  <td><div>
  <p>A NavigatorInterface implementation instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC5routeAA5RouteCSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-route" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC5routeAA5RouteCSgvp" class="token"><code>route</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="sdk-for-ios-explore-protocols-navigablelocationdelegate">`NavigableLocationDelegate`</a>. If set, both route progress (<a href="sdk-for-ios-explore-protocols-routeprogressdelegate">`RouteProgressDelegate`</a>) and route deviation (<a href="sdk-for-ios-explore-protocols-routedeviationdelegate">`RouteDeviationDelegate`</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var route: Route? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-route">Route</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24trackingTransportProfileAA0eF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trackingTransportProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24trackingTransportProfileAA0eF0VSgvp" class="token"><code>trackingTransportProfile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-ios-explore-structs-transportprofile">`TransportProfile`</a> can be defined with a <a href="sdk-for-ios-explore-structs-vehicleprofile">`VehicleProfile`</a>. A vehicle profile can have several parameters such as <a href="sdk-for-ios-explore-enums-vehicletype">`VehicleType`</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-ios-explore-enums-vehicletype#sdk-for-ios-explore-s-7heresdk11VehicleTypeO3caryA2CmF">`VehicleType.car`</a> profile.

  Currently used members of <a href="sdk-for-ios-explore-structs-transportprofile">`TransportProfile`</a>

  - <a href="sdk-for-ios-explore-enums-vehicletype">`VehicleType`</a>: Sets the transport mode.
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.")
  public var trackingTransportProfile: TransportProfile? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-transportprofile">TransportProfile</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30trackingTransportSpecificationAA0eF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trackingTransportSpecification" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30trackingTransportSpecificationAA0eF0VSgvp" class="token"><code>trackingTransportSpecification</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the transport specification for the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> must have the <a href="sdk-for-ios-explore-structs-transportspecification#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a> defined in <a href="sdk-for-ios-explore-structs-transportspecification#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> will have the transport mode set to <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.

  Currently used members of <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a>

  - <a href="sdk-for-ios-explore-structs-transportspecification#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a>: Sets the transport mode.
  - From <a href="sdk-for-ios-explore-structs-transportspecification#sdk-for-ios-explore-s-7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a>:
    - <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>: Required for truck related speed information.
    - <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">`VehicleSpecification.heightInCentimeters`</a>: Required for truck related speed information.
    - <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">`VehicleSpecification.widthInCentimeters`</a>: Additional truck definition for more specific truck speed information.
    - <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">`VehicleSpecification.lengthInCentimeters`</a>: Additional truck definition for more specific truck speed information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trackingTransportSpecification: TransportSpecification? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC25navigableLocationDelegateAA09NavigableeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-navigableLocationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC25navigableLocationDelegateAA09NavigableeF0_pSgvp" class="token"><code>navigableLocationDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-navigablelocationdelegate">NavigableLocationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC21routeProgressDelegateAA05RouteeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeProgressDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC21routeProgressDelegateAA05RouteeF0_pSgvp" class="token"><code>routeProgressDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-routeprogressdelegate">RouteProgressDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22routeDeviationDelegateAA05RouteeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeDeviationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22routeDeviationDelegateAA05RouteeF0_pSgvp" class="token"><code>routeDeviationDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-routedeviationdelegate">RouteDeviationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17eventTextDelegateAA05EventeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-eventTextDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17eventTextDelegateAA05EventeF0_pSgvp" class="token"><code>eventTextDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-eventtextdelegate">EventTextDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23milestoneStatusDelegateAA09MilestoneeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-milestoneStatusDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23milestoneStatusDelegateAA09MilestoneeF0_pSgvp" class="token"><code>milestoneStatusDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive notifications about the arrival at each <a href="sdk-for-ios-explore-structs-milestone">`Milestone`</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-ios-explore-enums-milestonetype#sdk-for-ios-explore-s-7heresdk13MilestoneTypeO8stopoveryA2CmF">`MilestoneType.stopover`</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-ios-explore-enums-milestonetype#sdk-for-ios-explore-s-7heresdk13MilestoneTypeO11passthroughyA2CmF">`MilestoneType.passthrough`</a> are excluded, by default, but can be included via <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC37isPassthroughWaypointsHandlingEnabledSbvp">`isPassthroughWaypointsHandlingEnabled`</a>. Milestone status notifications only occurs if a route has been set. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var milestoneStatusDelegate: MilestoneStatusDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC26destinationReachedDelegateAA011DestinationeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-destinationReachedDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC26destinationReachedDelegateAA011DestinationeF0_pSgvp" class="token"><code>destinationReachedDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-destinationreacheddelegate">DestinationReachedDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC20speedWarningDelegateAA05SpeedeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC20speedWarningDelegateAA05SpeedeF0_pSgvp" class="token"><code>speedWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-speedwarningdelegate">SpeedWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverViewLaneAssistanceDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC34maneuverViewLaneAssistanceDelegateAA08ManeuverefgH0_pSgvp" class="token"><code>maneuverViewLaneAssistanceDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-currentSituationLaneAssistanceViewDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC42currentSituationLaneAssistanceViewDelegateAA07CurrentefghI0_pSgvp" class="token"><code>currentSituationLaneAssistanceViewDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-environmentalZoneWarningListenerDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC40environmentalZoneWarningListenerDelegateAA013EnvironmentalefH0_pSgvp" class="token"><code>environmentalZoneWarningListenerDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-junctionViewLaneAssistanceDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC34junctionViewLaneAssistanceDelegateAA08JunctionefgH0_pSgvp" class="token"><code>junctionViewLaneAssistanceDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-safetyCameraWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27safetyCameraWarningDelegateAA06SafetyefG0_pSgvp" class="token"><code>safetyCameraWarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive safety camera warner notifications. If a delegate delegate is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">`SafetyCameraWarningDelegate`</a>. Setting `nil` value to the delegate will unset the delegate. It returns `nil` when no delegate is set by an user.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var safetyCameraWarningDelegate: SafetyCameraWarningDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC26safetyCameraWarningOptionsAA06SafetyefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-safetyCameraWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC26safetyCameraWarningOptionsAA06SafetyefG0Vvp" class="token"><code>safetyCameraWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Safety camera warning options to be passed to <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">`SafetyCameraWarningDelegate`</a>. These options allow the enabling or disabling the text notification for the warner.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var safetyCameraWarningOptions: SafetyCameraWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-dangerZoneWarningListenerDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC33dangerZoneWarningListenerDelegateAA06DangerefH0_pSgvp" class="token"><code>dangerZoneWarningListenerDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckRestrictionsWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC32truckRestrictionsWarningDelegateAA05TruckefG0_pSgvp" class="token"><code>truckRestrictionsWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC12warnerEngineAA06WarnerE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-warnerEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC12warnerEngineAA06WarnerE0Cvp" class="token"><code>warnerEngine</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-classes-warnerengine">WarnerEngine</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC31truckRestrictionsWarningOptionsAA05TruckefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckRestrictionsWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC31truckRestrictionsWarningOptionsAA05TruckefG0Vvp" class="token"><code>truckRestrictionsWarningOptions</code></a> 

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
  public var truckRestrictionsWarningOptions: TruckRestrictionsWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18postActionDelegateAA04PosteF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-postActionDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18postActionDelegateAA04PosteF0_pSgvp" class="token"><code>postActionDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-postactiondelegate">PostActionDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18speedLimitDelegateAA05SpeedeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedLimitDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18speedLimitDelegateAA05SpeedeF0_pSgvp" class="token"><code>speedLimitDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-speedlimitdelegate">SpeedLimitDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17roadTextsDelegateAA04RoadeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadTextsDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17roadTextsDelegateAA04RoadeF0_pSgvp" class="token"><code>roadTextsDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-roadtextsdelegate">RoadTextsDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22roadAttributesDelegateAA04RoadeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadAttributesDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22roadAttributesDelegateAA04RoadeF0_pSgvp" class="token"><code>roadAttributesDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-roadattributesdelegate">RoadAttributesDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23roadSignWarningDelegateAA04RoadefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadSignWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23roadSignWarningDelegateAA04RoadefG0_pSgvp" class="token"><code>roadSignWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22roadSignWarningOptionsAA04RoadefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadSignWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22roadSignWarningOptionsAA04RoadefG0Vvp" class="token"><code>roadSignWarningOptions</code></a> 

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
  public var roadSignWarningOptions: RoadSignWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-roadsignwarningoptions">RoadSignWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-schoolZoneWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC25schoolZoneWarningDelegateAA06SchoolefG0_pSgvp" class="token"><code>schoolZoneWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24schoolZoneWarningOptionsAA06SchoolefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-schoolZoneWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24schoolZoneWarningOptionsAA06SchoolefG0Vvp" class="token"><code>schoolZoneWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  School zone warning options It allow to configure school zone notifications to be passed to <a href="sdk-for-ios-explore-protocols-schoolzonewarningdelegate">`SchoolZoneWarningDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var schoolZoneWarningOptions: SchoolZoneWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28realisticViewWarningDelegateAA09RealisticefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-realisticViewWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28realisticViewWarningDelegateAA09RealisticefG0_pSgvp" class="token"><code>realisticViewWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27realisticViewWarningOptionsAA09RealisticefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-realisticViewWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27realisticViewWarningOptionsAA09RealisticefG0Vvp" class="token"><code>realisticViewWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Realistic view warning options. It allow to filter realistic views to be passed to <a href="sdk-for-ios-explore-protocols-realisticviewwarningdelegate">`RealisticViewWarningDelegate`</a>.

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC29borderCrossingWarningDelegateAA06BorderefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-borderCrossingWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC29borderCrossingWarningDelegateAA06BorderefG0_pSgvp" class="token"><code>borderCrossingWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28borderCrossingWarningOptionsAA06BorderefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-borderCrossingWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28borderCrossingWarningOptionsAA06BorderefG0Vvp" class="token"><code>borderCrossingWarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Border crossing warning options to be passed to <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">`BorderCrossingWarningDelegate`</a>. These options allow the filtering of the border crossing warnings received and set the notification distances.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var borderCrossingWarningOptions: BorderCrossingWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23tollStopWarningDelegateAA04TollefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tollStopWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23tollStopWarningDelegateAA04TollefG0_pSgvp" class="token"><code>tollStopWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-railwayCrossingWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30railwayCrossingWarningDelegateAA07RailwayefG0_pSgvp" class="token"><code>railwayCrossingWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lowSpeedZoneWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27lowSpeedZoneWarningDelegateAA03LowefgH0_pSgvp" class="token"><code>lowSpeedZoneWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficMergeWarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27trafficMergeWarningDelegateAA07TrafficefG0_pSgvp" class="token"><code>trafficMergeWarningDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC26trafficMergeWarningOptionsAA07TrafficefG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficMergeWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC26trafficMergeWarningOptionsAA07TrafficefG0Vvp" class="token"><code>trafficMergeWarningOptions</code></a> 

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
  public var trafficMergeWarningOptions: TrafficMergeWarningOptions { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-offRoadDestinationReachedDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC33offRoadDestinationReachedDelegateAA03OffefgH0_pSgvp" class="token"><code>offRoadDestinationReachedDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23offRoadProgressDelegateAA03OffefG0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-offRoadProgressDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23offRoadProgressDelegateAA03OffefG0_pSgvp" class="token"><code>offRoadProgressDelegate</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27maneuverNotificationOptionsAA08ManeuvereF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverNotificationOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27maneuverNotificationOptionsAA08ManeuvereF0Vvp" class="token"><code>maneuverNotificationOptions</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC16eventTextOptionsAA05EventeF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-eventTextOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC16eventTextOptionsAA05EventeF0Vvp" class="token"><code>eventTextOptions</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-eventtextoptions">EventTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC19speedWarningOptionsAA05SpeedeF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedWarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC19speedWarningOptionsAA05SpeedeF0Vvp" class="token"><code>speedWarningOptions</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-speedwarningoptions">SpeedWarningOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27isEnableTunnelExtrapolationSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isEnableTunnelExtrapolation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27isEnableTunnelExtrapolationSbvp" class="token"><code>isEnableTunnelExtrapolation</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC37isPassthroughWaypointsHandlingEnabledSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isPassthroughWaypointsHandlingEnabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC37isPassthroughWaypointsHandlingEnabledSbvp" class="token"><code>isPassthroughWaypointsHandlingEnabled</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14trafficOnRouteAA07TrafficeF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14trafficOnRouteAA07TrafficeF0VSgvp" class="token"><code>trafficOnRoute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic information for the current route. This impacts <a href="sdk-for-ios-explore-structs-routeprogress">`RouteProgress`</a> updates as the duration of the <a href="sdk-for-ios-explore-structs-sectionprogress">`SectionProgress`</a> might change. However, the remaining distance and the route geometry will remain unchanged.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficOnRoute: TrafficOnRoute? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficonroute">TrafficOnRoute</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC15locationManagerAA08LocationE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-locationManager" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC15locationManagerAA08LocationE0Cvp" class="token"><code>locationManager</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-classes-locationmanager">LocationManager</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14cameraBehaviorAA06CameraE0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-cameraBehavior" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14cameraBehaviorAA06CameraE0_pSgvp" class="token"><code>cameraBehavior</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera behavior which defines how the `VisualNavigator` handles the camera. Setting `nil` disables any camera behavior with the result that the camera does not follow the current location and keeps the last active camera state, i.e., current zoom and tilt. Furthermore, when `nil` is set map gestures can be used again to freely pan and zoom the map. In opposition, when a camera behavior is defined, then the map cannot be panned and zoomed by the user. The default value is an instance of <a href="sdk-for-ios-explore-classes-fixedcamerabehavior">`FixedCameraBehavior`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cameraBehavior: CameraBehavior? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-camerabehavior">CameraBehavior</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14isRouteVisibleSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isRouteVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14isRouteVisibleSbvp" class="token"><code>isRouteVisible</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-explore-classes-route">`Route`</a> visibility which defines whether to perform route rendering during visual navigation. When enabled, the set <a href="sdk-for-ios-explore-classes-route">`Route`</a> will be rendered as a <a href="sdk-for-ios-explore-classes-mappolyline">`MapPolyline`</a> together with <a href="sdk-for-ios-explore-classes-maparrow">`MapArrow`</a> items that indicate the next turns. By default, it is enabled. When disabled, <a href="sdk-for-ios-explore-classes-maparrow">`MapArrow`</a> items are still rendered. To hide arrows, use <a href="sdk-for-ios-explore-classes-visualnavigatorcolors">`VisualNavigatorColors`</a> with transparent color.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRouteVisible: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22isRouteProgressVisibleSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isRouteProgressVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22isRouteProgressVisibleSbvp" class="token"><code>isRouteProgressVisible</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-explore-structs-routeprogress">`RouteProgress`</a> visibility which defines whether to perform route progress coloring (“eat-up”) during visual navigation. By default, it is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRouteProgressVisible: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23isManeuverArrowsVisibleSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isManeuverArrowsVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23isManeuverArrowsVisibleSbvp" class="token"><code>isManeuverArrowsVisible</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maneuver arrows visibility which defines whether to perform maneuver arrow rendering during visual navigation. By default, it is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isManeuverArrowsVisible: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27isOffRoadDestinationVisibleSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isOffRoadDestinationVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC27isOffRoadDestinationVisibleSbvp" class="token"><code>isOffRoadDestinationVisible</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Off road destination visibility which defines whether to show a dashed line between the map-matched and the original destination which is off-road. By default it is enabled. **Note:** The dashed line will be drawn only if the original destination is off-road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isOffRoadDestinationVisible: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23isTrafficOnRouteVisibleSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isTrafficOnRouteVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23isTrafficOnRouteVisibleSbvp" class="token"><code>isTrafficOnRouteVisible</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A boolean which defines whether to perform rendering of traffic conditions on the route when <a href="sdk-for-ios-explore-classes-route">`Route`</a> visualization is enabled during visual navigation. When enabled the route’s <a href="sdk-for-ios-explore-classes-mappolyline">`MapPolyline`</a> will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in <a href="sdk-for-ios-explore-classes-visualnavigatorcolors#sdk-for-ios-explore-s-7heresdk21VisualNavigatorColorsC014trafficOnRouteD0AA07TrafficfgD0Vvp">`VisualNavigatorColors.trafficOnRouteColors`</a>. The presented traffic information is either set by the user via <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14trafficOnRouteAA07TrafficeF0VSgvp">`trafficOnRoute`</a> or is generated from historical traffic data stored in the map. **Note:** `VisualNavigator` does not perform automatic traffic data updates. The updated traffic information is available through the \[sdk.routing.RoutingEngine.calculate_traffic_on_route\] interface. The returned <a href="sdk-for-ios-explore-structs-trafficonroute">`TrafficOnRoute`</a> could then be used to update \[sdk.navigation.NavigatorInterface.traffic_on_route\] to refresh the traffic on route visualization. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTrafficOnRouteVisible: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-customLocationIndicator" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp" class="token"><code>customLocationIndicator</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Custom location indicator <a href="sdk-for-ios-explore-classes-locationindicator">`LocationIndicator`</a> which `VisualNavigator` uses instead of the default. If set, the user is responsible for adding and removing the object to/from the mapview. It is important to stop sending location updates to the provided <a href="sdk-for-ios-explore-classes-locationindicator">`LocationIndicator`</a>, since `VisualNavigator` will control its position when rendering is active, i.e., between startRendering(*) and stopRendering() calls. By default this property is `nil`, which means the default indicator is used, and `VisualNavigator` automatically adds and removes it to/from the mapview upon startRendering(*) and stopRendering() calls.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var customLocationIndicator: LocationIndicator? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-locationindicator">LocationIndicator</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28interpolatedLocationDelegateAA012InterpolatedeF0_pSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-interpolatedLocationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28interpolatedLocationDelegateAA012InterpolatedeF0_pSgvp" class="token"><code>interpolatedLocationDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to receive interpolated locations. For example, to pan a second instance of a <a href="sdk-for-ios-explore-protocols-mapviewbase">`MapViewBase`</a> or move additional markers smoothly. The map-matched locations are used if available, otherwise the non-map-matched ones are used instead. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public weak var interpolatedLocationDelegate: InterpolatedLocationDelegate? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-interpolatedlocationdelegate">InterpolatedLocationDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC11isRenderingSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isRendering" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC11isRenderingSbvp" class="token"><code>isRendering</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a value indicating whether visual navigation rendering is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRendering: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC6colorsAA0bC6ColorsCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-colors" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC6colorsAA0bC6ColorsCvp" class="token"><code>colors</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object containing colors used to render route progress and maneuver arrow visualization. Setting a new instance overwrites the default color settings as specified in <a href="sdk-for-ios-explore-classes-visualnavigatorcolors">`VisualNavigatorColors`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var colors: VisualNavigatorColors { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-visualnavigatorcolors">VisualNavigatorColors</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC21measureDependentWidthSDyAA10MapMeasureVSdGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-measureDependentWidth" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC21measureDependentWidthSDyAA10MapMeasureVSdGvp" class="token"><code>measureDependentWidth</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `measureDependentWidth` that defines the route and maneuver arrows width. It is a dictionary that has keys that are <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>s and values that are width in pixels at this <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>s. This route and maneuver arrows width is multiplied by a pixel_scale `pixelScale` before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24maneuverArrowWidthFactorSdvp">`VisualNavigator.maneuverArrowWidthFactor`</a>; which by default equals one. The function defined by a dictionary is linearly interpolated between each successive pair of data points. For keys below the lowest <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>, its corresponding value width is used. For keys above the highest <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>, its corresponding value width is used. Only <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a> of \[sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL\] type are supported. <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a> of other unsupported types will be ignored. `measureDependentWidth` with a single entry is equivalent to use of the constant width value of this single entry for all <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>s. Empty `measureDependentWidth` is ignored and existing dictionary of width is maintained. The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored. If route and maneuver arrows were not configured with this property, then `measureDependentWidth` contains predefined values chosen to be optimal for different route classes.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var measureDependentWidth: [MapMeasure : Double] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24maneuverArrowWidthFactorSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverArrowWidthFactor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC24maneuverArrowWidthFactorSdvp" class="token"><code>maneuverArrowWidthFactor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A factor of <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC21measureDependentWidthSDyAA10MapMeasureVSdGvp">`VisualNavigator.measureDependentWidth`</a> defining the width of the maneuver arrow. The factor should be positive. A value less than or equal to 0 is ignored. By default it is set to one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverArrowWidthFactor: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22isExtrapolationEnabledSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isExtrapolationEnabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC22isExtrapolationEnabledSbvp" class="token"><code>isExtrapolationEnabled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines whether the position extrapolation logic is enabled or not. The predicted location follows the geometry of the route (or road) ahead. By default it is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isExtrapolationEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC16debugGpxFilePathSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-debugGpxFilePath" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC16debugGpxFilePathSSSgvp" class="token"><code>debugGpxFilePath</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Show the contents of a GPX file on the map. **Note:** This API should be used for debugging purposes only.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var debugGpxFilePath: String? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18isDebugModeEnabledSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isDebugModeEnabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18isDebugModeEnabledSbvp" class="token"><code>isDebugModeEnabled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When enabled, it shows useful information for debugging purposes.

  - A semi-transparent location marker indicating the map-matched location.
  - A gray, semi-transparent location marker indicating the raw (or original) input location.
  - A red polyline indicating the most probable path.
  - A SVG overlay, on the middle-left of the screen, showing the following:
    - IN - Input location: coordinates \[bearing\] \[speed\] \[accuracy\]
    - RM - Route-matched location: coordinates bearing (distance-to-raw-location)
    - MM - Map-Matched location: coordinates bearing (distance-to-raw-location)
    - RM-MM - distance-between-route-and-map-matched-locations
    - RP - Route progress: remaining-duration remaining-distance
    - SP - Section progress: section-index/sections-count remaining-duration remaining-distance
    - MP - Maneuver progress: maneuver-index remaining-duration remaining-distance
    - CPU - CPU usage: cpu-usage current-date-time
    - MS - Milestone status: section-index MISSED\|REACHED when
    - RD - Route deviation: last-traveled-section-index last-traveled-section-distance when
    - FPS - Frames per second: frames-per-second

  Fields between brackets (\[\]‘s) are omitted if not available.

  Example:

      IN: 53.96880,14.77903 167° 8m/s
      RM: 53.96880,14.77903 167° (0.0m)
      MM: 53.96879,14.77903 167° (0.5m)
      RM-MM: 0.5m
      RP: 49h0m3s 4302km
      SP: 0/16 1h2m20s 58km
      MP: 1 5s 25m
      CPU: 7% 2024-01-01 13:21:59
      MS: 1 REACHED 12:34:22
      RD: 2 345m 11:13:55
      FPS: 30.0

  **Note:** This API should be used for debugging purposes only.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDebugModeEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28isLocationAccuracyVisualizedSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isLocationAccuracyVisualized" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC28isLocationAccuracyVisualizedSbvp" class="token"><code>isLocationAccuracyVisualized</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls if the halo accuracy visualization of the default <a href="sdk-for-ios-explore-classes-locationindicator">`LocationIndicator`</a> is rendered or not. Does not affect halo accuracy indicator of the <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp">`VisualNavigator.customLocationIndicator`</a>. If <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC23customLocationIndicatorAA0eF0CSgvp">`VisualNavigator.customLocationIndicator`</a> is set, then its halo accuracy indicator can be controlled using <a href="sdk-for-ios-explore-classes-locationindicator#sdk-for-ios-explore-s-7heresdk17LocationIndicatorC20isAccuracyVisualizedSbvp">`LocationIndicator.isAccuracyVisualized`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isLocationAccuracyVisualized: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC25isDynamicFrameRateEnabledSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isDynamicFrameRateEnabled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC25isDynamicFrameRateEnabledSbvp" class="token"><code>isDynamicFrameRateEnabled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Flag used to enable or disable the dynamic frame rate. Controls whether the number of map updates is dynamically calculated based on the current zoom level. If the zoom level is low, i.e., the camera target distance is high, updates to LocationIndicator, MapCamera and MapPolylines representing the route progress will happen less frequent. It is on by default.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDynamicFrameRateEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-guidanceFrameRate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp" class="token"><code>guidanceFrameRate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Frame rate used during guidance. Frame rate used during guidance. Default is 30fps.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var guidanceFrameRate: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14routeDrawOrders5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeDrawOrder" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14routeDrawOrders5Int32Vvp" class="token"><code>routeDrawOrder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The draw order of the polylines representing the route. The draw order of the polylines representing the route. For more details see <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC9drawOrders5Int32Vvp">`MapPolyline.drawOrder`</a>. The default is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeDrawOrder: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18routeDrawOrderTypeAA0efG0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeDrawOrderType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC18routeDrawOrderTypeAA0efG0Ovp" class="token"><code>routeDrawOrderType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The draw order type of the polylines representing the route. The draw order type of the polylines representing the route. For more details see <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp">`MapPolyline.drawOrderType`</a>. The default is <a href="sdk-for-ios-explore-enums-drawordertype#sdk-for-ios-explore-s-7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderDependent`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeDrawOrderType: DrawOrderType { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-drawordertype">DrawOrderType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC11getManeuver5indexAA0E0CSgs5Int32V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getManeuver-index" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC11getManeuver5indexAA0E0CSgs5Int32V_tF" class="token"><code>getManeuver(index:</code><wbr></wbr><code>)</code></a> 

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
  public func getManeuver(index: Int32) -> Maneuver?
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getManeuverNotificationTimingOptions-transportMode-timingProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC36getManeuverNotificationTimingOptions13transportMode13timingProfileAA0efgH0VAA09TransportJ0O_AA0gL0OtF" class="token"><code>getManeuverNotificationTimingOptions(transportMode:</code><wbr></wbr><code>timingProfile:</code><wbr></wbr><code>)</code></a> 

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
  public func getManeuverNotificationTimingOptions(transportMode: TransportMode, timingProfile: TimingProfile) -> ManeuverNotificationTimingOptions
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setManeuverNotificationTimingOptions-transportMode-timingProfile-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC36setManeuverNotificationTimingOptions13transportMode13timingProfile7optionsSbAA09TransportJ0O_AA0gL0OAA0efgH0VtF" class="token"><code>setManeuverNotificationTimingOptions(transportMode:</code><wbr></wbr><code>timingProfile:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

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
  public func setManeuverNotificationTimingOptions(transportMode: TransportMode, timingProfile: TimingProfile, options: ManeuverNotificationTimingOptions) -> Bool
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getWarningNotificationDistances-warningType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF" class="token"><code>getWarningNotificationDistances(warningType:</code><wbr></wbr><code>)</code></a> 

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
  public func getWarningNotificationDistances(warningType: WarningType) -> WarningNotificationDistances
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setWarningNotificationDistances-warningType-warningNotificationDistances" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF" class="token"><code>setWarningNotificationDistances(warningType:</code><wbr></wbr><code>warningNotificationDistances:</code><wbr></wbr><code>)</code></a> 

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
  public func setWarningNotificationDistances(warningType: WarningType, warningNotificationDistances: WarningNotificationDistances) -> Bool
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30repeatLastManeuverNotificationyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-repeatLastManeuverNotification" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30repeatLastManeuverNotificationyyF" class="token"><code>repeatLastManeuverNotification()</code></a> 

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
  public func repeatLastManeuverNotification()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRemainingDistanceInMeters-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC34calculateRemainingDistanceInMeters11coordinatess5Int32VSgAA14GeoCoordinatesV_tF" class="token"><code>calculateRemainingDistanceInMeters(coordinates:</code><wbr></wbr><code>)</code></a> 

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
  public func calculateRemainingDistanceInMeters(coordinates: GeoCoordinates) -> Int32?
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC15setCustomOption3key5valueySS_SStF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCustomOption-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC15setCustomOption3key5valueySS_SStF" class="token"><code>setCustomOption(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

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
  public func setCustomOption(key: String, value: String)
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

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17onLocationUpdatedyyAA0E0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onLocationUpdated-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC17onLocationUpdatedyyAA0E0VF" class="token"><code>onLocationUpdated(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time a new location is available. In a navigation context while using the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a> or `VisualNavigator`, it’s required to set the <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object so that the HERE SDK can map-match the locations properly. If the <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onLocationUpdated(_ location: Location)
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

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC42availableLanguagesForManeuverNotificationsSayAA12LanguageCodeOGyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-availableLanguagesForManeuverNotifications" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC42availableLanguagesForManeuverNotificationsSayAA12LanguageCodeOGyFZ" class="token"><code>availableLanguagesForManeuverNotifications()</code></a> 

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
  public static func availableLanguagesForManeuverNotifications() -> [LanguageCode]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-languagecode">LanguageCode</a>

  </div>

  <div>

  #### Return Value

  the list of languages for maneuver notification currently available in the SDK.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-startRendering-mapView" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF" class="token"><code>startRendering(mapView:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts visual navigation rendering. A preconfigured current location marker is shown as soon as a location is received. The marker is chosen according to the transport mode specified in the route. If no route is present, the marker is chosen based on the <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC30trackingTransportSpecificationAA0eF0VSgvp">`trackingTransportSpecification`</a> property. Calling startRendering(\_) changes the <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC14principalPointAA7Point2DVvp">`MapCamera.principalPoint`</a> property so that the current position indicator is equal to the value from \[sdk.navigation.CameraBehavior.normalized_principal_point\], in which by default places the principal point slightly at the bottom of the mapview. It is restored to its original value when stopRendering() is called. **Note:** When rendering is started again for a new map view instance, rendering is automatically stopped on the previous map view instance. Also note that the `frameRate` can be lowered to reduce CPU usage, to adjust for tradeoffs between rendering smoothness versus battery consumption.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func startRendering(mapView: MapViewBase)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapviewbase">MapViewBase</a>

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
  <td><code> </code><em><code>mapView</code></em><code> </code></td>
  <td><div>
  <p>The map view on which visual navigation will take place.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC13stopRenderingyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-stopRendering" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC13stopRenderingyyF" class="token"><code>stopRendering()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stops visual navigation rendering. This removes the current location marker. Other settings, like map orientation or camera distance, which may have been altered during rendering are no longer updated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func stopRendering()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VisualNavigatorC47defaultRouteManeuverArrowMeasureDependentWidthsSDyAA03MapH0VSdGyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-defaultRouteManeuverArrowMeasureDependentWidths" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-visualnavigator#sdk-for-ios-explore-s-7heresdk15VisualNavigatorC47defaultRouteManeuverArrowMeasureDependentWidthsSDyAA03MapH0VSdGyFZ" class="token"><code>defaultRouteManeuverArrowMeasureDependentWidths()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves a dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>s.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func defaultRouteManeuverArrowMeasureDependentWidths() -> [MapMeasure : Double]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>

  </div>

  <div>

  #### Return Value

  A dictionary of default route and maneuver arrow widths as a function of <a href="sdk-for-ios-explore-structs-mapmeasure">`MapMeasure`</a>s.

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

