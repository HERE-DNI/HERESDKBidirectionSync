---
title: "ElectronicHorizonEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary">com.here.sdk.electronichorizon</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.electronichorizon.ElectronicHorizonEngine → com.here.NativeBase com.here.sdk.electronichorizon.ElectronicHorizonEngine → com.here.sdk.electronichorizon.ElectronicHorizonEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ElectronicHorizonEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight. You can subscribe to electronic horizon updates based on position updates by using ElectronicHorizonListener . For more information about sub path levels, see ElectronicHorizonOptions.lookAheadDistancesInMeters . The electronic horizon engine uses map-matched locations and can optionally use a Route to improve the most-preferred path (MPP). Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      ElectronicHorizonEngine ( SDKNativeEngine sdkEngine, ElectronicHorizonOptions options, TransportMode transportMode, Route route)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of ElectronicHorizonEngine .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addElectronicHorizonListener ( ElectronicHorizonListener electronicHorizonListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds an ElectronicHorizonListener to the subscription list.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoute ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the instance of Route or null if Route is not set.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeElectronicHorizonListener ( ElectronicHorizonListener electronicHorizonListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes an ElectronicHorizonListener from the subscription list.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoute ( Route value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the instance of Route to be used by ElectronicHorizonEngine or null if no route should be used.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      update ( MapMatchedLocation mapMatchedLocation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Updates the electronic horizon paths based on the provided map-matched location.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-electronichorizon-ElectronicHorizonOptions-com-here-sdk-transport-TransportMode-com-here-sdk-routing-Route" class="section detail">

    ### ElectronicHorizonEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ElectronicHorizonEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of ElectronicHorizonEngine .

    </div>

    Parameters:  
    `sdkEngine` -

    The <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">`SDKNativeEngine`</a> instance that provides shared services, such as networking and map data.

    `options` -

    The <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">`ElectronicHorizonOptions`</a> instance that configures how the electronic horizon is calculated, including look-ahead distances.

    `transportMode` -

    The <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">`TransportMode`</a> that is used when building the electronic horizon paths.

    `route` -

    The <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a> that improves the calculation of the most-preferred path (MPP). If `null` is passed, the most-preferred path can deviate from the route.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> If the electronic horizon engine cannot be created.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-update-com-here-sdk-navigation-MapMatchedLocation" class="section detail">

    ### update

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a> mapMatchedLocation)</span>

    </div>

    <div class="block">

    Updates the electronic horizon paths based on the provided map-matched location. This method returns immediately and does not block. When internal calculation is complete, callbacks are called on the main thread. When multiple updates are triggered while processing is still running, intermediate locations are skipped and only the last location is processed.

    </div>

    Parameters:  
    `mapMatchedLocation` -

    The map-matched location that defines the current vehicle position on the road network.

    </div>

  - <div id="sdk-for-android-navigate-addElectronicHorizonListener-com-here-sdk-electronichorizon-ElectronicHorizonListener" class="section detail">

    ### addElectronicHorizonListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addElectronicHorizonListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</span>

    </div>

    <div class="block">

    Adds an ElectronicHorizonListener to the subscription list.

    </div>

    Parameters:  
    `electronicHorizonListener` -

    The listener that receives electronic horizon path updates.

    </div>

  - <div id="sdk-for-android-navigate-removeElectronicHorizonListener-com-here-sdk-electronichorizon-ElectronicHorizonListener" class="section detail">

    ### removeElectronicHorizonListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElectronicHorizonListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a> electronicHorizonListener)</span>

    </div>

    <div class="block">

    Removes an ElectronicHorizonListener from the subscription list.

    </div>

    Parameters:  
    `electronicHorizonListener` -

    The listener that should no longer receive electronic horizon path updates.

    </div>

  - <div id="sdk-for-android-navigate-getRoute" class="section detail">

    ### getRoute

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">getRoute</span>()

    </div>

    <div class="block">

    Gets the instance of Route or null if Route is not set. You can override this property to rebuild the electronic horizon based on a different route.

    </div>

    Returns:  
    The instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a> that is being used by <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon">`ElectronicHorizonEngine`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setRoute-com-here-sdk-routing-Route" class="section detail">

    ### setRoute

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoute</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> value)</span>

    </div>

    <div class="block">

    Sets the instance of Route to be used by ElectronicHorizonEngine or null if no route should be used. You can override this property to rebuild the electronic horizon based on a different route.

    </div>

    Parameters:  
    `value` -

    The instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a> that is being used by <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon">`ElectronicHorizonEngine`</a>.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

