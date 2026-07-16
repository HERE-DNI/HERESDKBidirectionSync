---
title: "RefreshRouteOptions Class Reference"
slug: "sdk-for-ios-explore-classes-refreshrouteoptions"
---

# RefreshRouteOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use the `RoutingOptions` class instead.")
public class RefreshRouteOptions
```

``` highlight
extension RefreshRouteOptions: NativeBase
```

``` highlight
extension RefreshRouteOptions: Hashable
```

</div>

</div>

The options to specify how to refresh an already calculated route identified by a <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a>. All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV12alternativess5Int32Vvp">`RouteOptions.alternatives`</a>, <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">`RouteOptions.arrivalTime`</a>, and <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a>. If new <a href="sdk-for-ios-explore-structs-avoidanceoptions">`AvoidanceOptions`</a> are specified, they are ignored as well and instead new <a href="sdk-for-ios-explore-structs-sectionnotice">`SectionNotice`</a>‘s are generated that indicate where the requested <a href="sdk-for-ios-explore-structs-avoidanceoptions">`AvoidanceOptions`</a> are violated. Note that when <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18ensureReachabilitySbvp">`EVCarOptions.ensureReachability`</a> is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA13TransportModeOcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA13TransportModeOcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-enums-transportmode">`TransportMode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ transportMode: TransportMode)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>

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
  <p>Updates the transport mode for the route.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA03CarD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA03CarD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-caroptions">`CarOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ carOptions: CarOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>

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
  <td><code> </code><em><code>carOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a car route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA05TruckD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA05TruckD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-truckoptions">`TruckOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ truckOptions: TruckOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>

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
  <td><code> </code><em><code>truckOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a truck route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA010PedestrianD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA010PedestrianD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-pedestrianoptions">`PedestrianOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ pedestrianOptions: PedestrianOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-pedestrianoptions">PedestrianOptions</a>

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
  <td><code> </code><em><code>pedestrianOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a pedestrian route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA07ScooterD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA07ScooterD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-scooteroptions">`ScooterOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ scooterOptions: ScooterOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-scooteroptions">ScooterOptions</a>

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
  <td><code> </code><em><code>scooterOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a scooter route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA04TaxiD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA04TaxiD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-taxioptions">`TaxiOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ taxiOptions: TaxiOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-taxioptions">TaxiOptions</a>

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
  <td><code> </code><em><code>taxiOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a taxi route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA05EVCarD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA05EVCarD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-evcaroptions">`EVCarOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ evCarOptions: EVCarOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>

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
  <td><code> </code><em><code>evCarOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to an electric car route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA07EVTruckD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA07EVTruckD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-evtruckoptions">`EVTruckOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ evTruckOptions: EVTruckOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>

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
  <td><code> </code><em><code>evTruckOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to an electric truck route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA07BicycleD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA07BicycleD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-bicycleoptions">`BicycleOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ bicycleOptions: BicycleOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-bicycleoptions">BicycleOptions</a>

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
  <td><code> </code><em><code>bicycleOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a bicycle route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA03BusD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA03BusD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-busoptions">`BusOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ busOptions: BusOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-busoptions">BusOptions</a>

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
  <td><code> </code><em><code>busOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a bus route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA010PrivateBusD0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-refreshrouteoptions#sdk-for-ios-explore-s-7heresdk19RefreshRouteOptionsCyAcA010PrivateBusD0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-explore-structs-privatebusoptions">`PrivateBusOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ privateBusOptions: PrivateBusOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-privatebusoptions">PrivateBusOptions</a>

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
  <td><code> </code><em><code>privateBusOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a private bus route, if a different transport mode was used for the <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
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

