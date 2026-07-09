---
title: "TrafficBroadcast (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcast"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-package-summary">com.here.sdk.trafficbroadcast</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.trafficbroadcast.TrafficBroadcast → com.here.NativeBase com.here.sdk.trafficbroadcast.TrafficBroadcast → com.here.sdk.trafficbroadcast.TrafficBroadcast

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficBroadcast</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span>

</div>

<div class="block">

A TrafficBroadcast is expecting the RDS-TMC format and it can be used when there is no internet connection, so that the OfflineRoutingEngine can utilize traffic data coming over a radio channel. The activate() method needs to be called to receive traffic data events. Note: In order to adopt the TrafficDataProvider interface special hardware is required. Talk to your HERE representative for more details. Only by adopting the TrafficDataProvider interface you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant to be used independently from the already included traffic on routes, on the map and from the HERE backends (when using the TrafficEngine ). This class continuously reacts to new locations provided from a location source and acts as a LocationListener . The location must be updated regardless of calling activate() . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      TrafficBroadcast ( SDKNativeEngine sdkEngine, TrafficBroadcastParameters parameters)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      TrafficBroadcast ( TrafficBroadcastParameters parameters)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

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

      activate ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Activates the reception of traffic data over the radio channel.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      deactivate ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Deactivates the reception of traffic data over the radio channel.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">`TrafficDataProvider`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficDataProvider ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onLocationUpdated ( Location location)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Called each time a new location is available.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onTMCDataUpdated ( TMCData tmcData)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Must be called on every TMC data update.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onTMCServiceProviderInfoUpdated ( TMCServiceProviderInfo tmcServiceProdiverInfo)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Must be called on every TMC service prodiver info update.

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-trafficbroadcast-TrafficBroadcastParameters" class="section detail">

    ### TrafficBroadcast

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficBroadcast</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a> parameters)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `parameters` -

    The necessary parameters to start traffic broadcast.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    when the object was not initialized properly.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-trafficbroadcast-TrafficBroadcastParameters" class="section detail">

    ### TrafficBroadcast

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficBroadcast</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a> parameters)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    `parameters` -

    The necessary parameters to start traffic broadcast.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    when the object was not initialized properly.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-activate" class="section detail">

    ### activate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">activate</span>()

    </div>

    <div class="block">

    Activates the reception of traffic data over the radio channel. This method is supposed to be called when the system loses internet connection, so that traffic data can be switched from the online source to the radio channel. When activation is done, requestTMCService is called from TMCServiceInterface

    </div>

    </div>

  - <div id="sdk-for-android-navigate-deactivate" class="section detail">

    ### deactivate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deactivate</span>()

    </div>

    <div class="block">

    Deactivates the reception of traffic data over the radio channel. When deactivation is done, requestTMCService is called from TMCServiceInterface With special case of countryCode parameter = 0

    </div>

    </div>

  - <div id="sdk-for-android-navigate-onTMCServiceProviderInfoUpdated-com-here-sdk-trafficbroadcast-TMCServiceProviderInfo" class="section detail">

    ### onTMCServiceProviderInfoUpdated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onTMCServiceProviderInfoUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceproviderinfo" title="class in com.here.sdk.trafficbroadcast">TMCServiceProviderInfo</a> tmcServiceProdiverInfo)</span>

    </div>

    <div class="block">

    Must be called on every TMC service prodiver info update.

    </div>

    Parameters:  
    `tmcServiceProdiverInfo` -

    Contains service prodiver info in RDS-TMC format.

    </div>

  - <div id="sdk-for-android-navigate-onTMCDataUpdated-com-here-sdk-trafficbroadcast-TMCData" class="section detail">

    ### onTMCDataUpdated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onTMCDataUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcdata" title="class in com.here.sdk.trafficbroadcast">TMCData</a> tmcData)</span>

    </div>

    <div class="block">

    Must be called on every TMC data update.

    </div>

    Parameters:  
    `tmcData` -

    Contains the traffic events in RDS-TMC format.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficDataProvider" class="section detail">

    ### getTrafficDataProvider

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></span> <span class="element-name">getTrafficDataProvider</span>()

    </div>

    Returns:  
    The traffic data provider that provides the traffic information.

    </div>

  - <div id="sdk-for-android-navigate-onLocationUpdated-com-here-sdk-core-Location" class="section detail">

    ### onLocationUpdated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span>

    </div>

    <div class="block">

    Called each time a new location is available. In a navigation context while using the Navigator or VisualNavigator , it's required to set the Location.time parameter for each Location object so that the HERE SDK can map-match the locations properly. If the Location.time parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the bearing and speed parameters for each Location object. Invoked on the main thread.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener#onLocationUpdated(com.here.sdk.core.Location">`onLocationUpdated`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

    Parameters:  
    `location` -

    Current location.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

