---
title: "ElectricVehicleOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.ElectricVehicleOptions → com.here.sdk.routing.ElectricVehicleOptions

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ElectricVehicleOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

These options define the parameters of the electric vehicle. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#batterySpecifications" class="member-name-link"><code>batterySpecifications</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Parameters that describe the electric vehicle's battery.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`EmpiricalConsumptionModel`](sdk-for-android-explore-com-here-sdk-routing-empiricalconsumptionmodel "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#empiricalConsumptionModel" class="member-name-link"><code>empiricalConsumptionModel</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the empirical consumption model.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#ensureReachability" class="member-name-link"><code>ensureReachability</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Ensure that the vehicle does not run out of energy along the way.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`EVMobilityServiceProviderPreferences`](sdk-for-android-explore-com-here-sdk-routing-evmobilityserviceproviderpreferences "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#evMobilityServiceProviderPreferences" class="member-name-link"><code>evMobilityServiceProviderPreferences</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the preferred E-Mobility Service Providers.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`PhysicalConsumptionModel`](sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#physicalConsumptionModel" class="member-name-link"><code>physicalConsumptionModel</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the physical consumption model.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      ElectricVehicleOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-ensureReachability" class="section detail">

    ### ensureReachability

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">ensureReachability</span>

    </div>

    <div class="block">

    Ensure that the vehicle does not run out of energy along the way. Requires valid battery_specifications . It also requires that RouteOptions.optimizationMode = OptimizationMode.FASTEST , RouteOptions.speedCapInMetersPerSecond is not set, and AvoidanceOptions is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. Note An RoutingError.INVALID_PARAMETER is generated when this option is set to true in case sdk.routing.RoutingEngine.import_route is called. Defaults to false . Note Not supported for offline routing. Note Only supported for car routing.

    </div>

    </div>

  - <div id="sdk-for-android-explore-evMobilityServiceProviderPreferences" class="section detail">

    ### evMobilityServiceProviderPreferences

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[EVMobilityServiceProviderPreferences](sdk-for-android-explore-com-here-sdk-routing-evmobilityserviceproviderpreferences "class in com.here.sdk.routing")</span> <span class="element-name">evMobilityServiceProviderPreferences</span>

    </div>

    <div class="block">

    Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html An alternative way to get partnerId is the eMobilityServiceProviders.partnerId as part of HERE SDK Search . Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used. Note Not yet supported for offline routing.

    </div>

    </div>

  - <div id="sdk-for-android-explore-empiricalConsumptionModel" class="section detail">

    ### empiricalConsumptionModel

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[EmpiricalConsumptionModel](sdk-for-android-explore-com-here-sdk-routing-empiricalconsumptionmodel "class in com.here.sdk.routing")</span> <span class="element-name">empiricalConsumptionModel</span>

    </div>

    <div class="block">

    Defines the empirical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. Note Only one consumption model is supported per route.

    </div>

    </div>

  - <div id="sdk-for-android-explore-physicalConsumptionModel" class="section detail">

    ### physicalConsumptionModel

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[PhysicalConsumptionModel](sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel "class in com.here.sdk.routing")</span> <span class="element-name">physicalConsumptionModel</span>

    </div>

    <div class="block">

    Defines the physical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. Note Only one consumption model is supported per route.

    </div>

    </div>

  - <div id="sdk-for-android-explore-batterySpecifications" class="section detail">

    ### batterySpecifications

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[BatterySpecifications](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing")</span> <span class="element-name">batterySpecifications</span>

    </div>

    <div class="block">

    Parameters that describe the electric vehicle's battery. By default, it is set to null .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### ElectricVehicleOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ElectricVehicleOptions</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

