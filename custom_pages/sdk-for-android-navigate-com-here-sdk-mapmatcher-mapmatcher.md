---
title: "MapMatcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-package-summary">com.here.sdk.mapmatcher</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapmatcher.MapMatcher → com.here.NativeBase com.here.sdk.mapmatcher.MapMatcher → com.here.sdk.mapmatcher.MapMatcher

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapMatcher</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

This class provides map-matching functionality. It determines whether a location can be matched to a nearby road network and provides additional OCM map data for that location. Note: This is a beta release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process. A MapMatcher maintains an internal state across location updates. This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy of the provided location. A MapMatcher requires OCM tile data, either through caching, prefetching, or installed Region data. If the necessary tiles are not found, an online request is initiated. Note that in such cases, the download is triggered silently in the background, and null is returned immediately. The MapMatcher supports two layer configurations for retrieving segment geometry data: Rendering layer ( LayerConfiguration.Feature.RENDERING ) : Enabled by default. If your application uses map rendering or MapView components, using this layer is recommended. eHorizon layer ( LayerConfiguration.Feature.EHORIZON ) : Not enabled by default. It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data. Use the eHorizon layer when: No MapView is used in your application. Only the eHorizon layer is used in your application. In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download. Important : If useRenderingLayers is set to false without properly enabling the eHorizon layer, it may produce incorrect results. Layer configuration is especially important when prefetching or installing region data. Missing data will be downloaded online automatically as needed. If your hardware supports pitch and high precision altitude information and you want to use them in the MapMatcher to improve map-matching, then enable the LayerConfiguration.Feature.ADAS layer: Turn on the ADAS layer via LayerConfiguration.enabledFeatures (it will increase data consumption). If available, set location.pitchInDegrees , location.coordinates.altitude and location.verticalAccuracyInMeters . In case of issues, please contact your HERE representative.

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

      MapMatcher ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMatcher ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapMatcher ( SDKNativeEngine sdkEngine,
       boolean useRenderingLayers)

  </div>

  <div class="col-last even-row-color">

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">`MapMatchedLocation`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      match ( Location location)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  This method computes the map-matched location for the provided input location.

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

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### MapMatcher

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMatcher</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### MapMatcher

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMatcher</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    A SDKEngine instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-boolean" class="section detail">

    ### MapMatcher

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMatcher</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, boolean useRenderingLayers)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    A SDKEngine instance.

    `useRenderingLayers` -

    When set to true, `LayerConfiguration.Feature.RENDERING` is used; otherwise, `LayerConfiguration.Feature.EHORIZON` is used to retrieve segment geometry data from the OCM map. Note: Ensure the corresponding layer is properly enabled in your `LayerConfiguration` to avoid incorrect results.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-match-com-here-sdk-core-Location" class="section detail">

    ### match

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a></span> <span class="element-name">match</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span>

    </div>

    <div class="block">

    This method computes the map-matched location for the provided input location. Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found within that radius, null is returned. It's required to set time field for each Location object for the MapMatcher to work properly. In case no time is provided, null is returned and an error message is logged. It is used to calculate the distance in time between consecutive matches. Together with speed , this allows to calculate how likely a match is consistent with a previous match. To improve matching accuracy, it is recommended to provide bearing and speed parameters for each Location object.

    </div>

    Parameters:  
    `location` -

    The input location.

    Returns:  
    map-matched location or `null` if the location could not be matched to a road network.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

