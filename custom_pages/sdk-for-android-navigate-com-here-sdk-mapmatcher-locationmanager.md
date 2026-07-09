---
title: "LocationManager (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-package-summary">com.here.sdk.mapmatcher</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapmatcher.LocationManager → com.here.NativeBase com.here.sdk.mapmatcher.LocationManager → com.here.sdk.mapmatcher.LocationManager

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LocationManager</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span>

</div>

<div class="block">

LocationManager listens to position updates and provides the map-matched location using the LocationManagerListener. Note: This is a beta release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

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

      LocationManager ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of LocationManager .

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

      addMatchedLocationListener ( MatchedLocationListener matchedLocationListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds the MatchedLocationListener to the subscribtion list.

  </div>

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

      removeMatchedLocationListener ( MatchedLocationListener matchedLocationListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes the MatchedLocationListener from the subscribtion list.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMapMatcher ( MapMatcher mapMatcher)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the MapMatcher for exclusive use by LocationManager .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">`MapMatcher`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      takeMapMatcher ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Retrieves and removes the MapMatcher from LocationManager .

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### LocationManager

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationManager</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of LocationManager .

    </div>

    Parameters:  
    `sdkEngine` -

    A SDKEngine instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Instantiation error.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-setMapMatcher-com-here-sdk-mapmatcher-MapMatcher" class="section detail">

    ### setMapMatcher

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMapMatcher</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a> mapMatcher)</span>

    </div>

    <div class="block">

    Sets the MapMatcher for exclusive use by LocationManager . Threading: This method is asynchronous and performs the switch in an internal thread of LocationManager . Note: After calling this method, the MapMatcher is owned and used exclusively by LocationManager in its internal processing thread. Do not use or access the MapMatcher elsewhere while it is set.

    </div>

    Parameters:  
    `mapMatcher` -

    The <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">`MapMatcher`</a> instance to be used exclusively by <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">`LocationManager`</a>.

    </div>

  - <div id="sdk-for-android-navigate-takeMapMatcher" class="section detail">

    ### takeMapMatcher

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">MapMatcher</a></span> <span class="element-name">takeMapMatcher</span>()

    </div>

    <div class="block">

    Retrieves and removes the MapMatcher from LocationManager . Note: After calling this method, LocationManager will no longer use the MapMatcher at all. the caller regains full ownership and responsibility for the MapMatcher .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher" title="class in com.here.sdk.mapmatcher">`MapMatcher`</a> instance previously set, or `null` if none was set.

    </div>

  - <div id="sdk-for-android-navigate-addMatchedLocationListener-com-here-sdk-mapmatcher-MatchedLocationListener" class="section detail">

    ### addMatchedLocationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addMatchedLocationListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</span>

    </div>

    <div class="block">

    Adds the MatchedLocationListener to the subscribtion list.

    </div>

    Parameters:  
    `matchedLocationListener` -

    Listener to be added to the map matched location updates.

    </div>

  - <div id="sdk-for-android-navigate-removeMatchedLocationListener-com-here-sdk-mapmatcher-MatchedLocationListener" class="section detail">

    ### removeMatchedLocationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeMatchedLocationListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener" title="interface in com.here.sdk.mapmatcher">MatchedLocationListener</a> matchedLocationListener)</span>

    </div>

    <div class="block">

    Removes the MatchedLocationListener from the subscribtion list.

    </div>

    Parameters:  
    `matchedLocationListener` -

    Listener to be removed from the map matched location updates.

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

