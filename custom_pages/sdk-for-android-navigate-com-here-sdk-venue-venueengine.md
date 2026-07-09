---
title: "VenueEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-venueengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-package-summary">com.here.sdk.venue</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.VenueEngine → com.here.NativeBase com.here.sdk.venue.VenueEngine → com.here.sdk.venue.VenueEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VenueEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

VenueEngine is an add-on to the base map functionality with its own content loading and cache. VenueEngine gives access to the venue functionality, which allows you to load and visualize venues on the map, search content inside venues etc.

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

      VenueEngine ( SDKNativeEngine sdkEngine, VenueEngineInitCallback callback)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      VenueEngine ( VenueEngineInitCallback callback)

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

      destroy ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Releases all internally used resources.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control">`VenueMap`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueMap ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a venue map to visualize venues.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">`VenueService`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueService ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the venue service.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( AuthenticationCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Authenticates asynchronously using HERE SDK credentials and uses a result token to start the VenueService .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( String token)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Authenticates asynchronously using HERE SDK credentials using a token to start the VenueService .

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-venue-VenueEngineInitCallback" class="section detail">

    ### VenueEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VenueEngine</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `callback` -

    The optional callback that will be triggered when a venue engine initialization will be completed. After the initialization, the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">`VenueService`</a> should be started using one of its methods or using [](sdk-for-android-navigate-com-here-sdk-venue-venueengine#start(java.lang.String))

        start(String)

    </a>.

    </p>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-venue-VenueEngineInitCallback" class="section detail">

    ### VenueEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">VenueEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-venueengineinitcallback" title="interface in com.here.sdk.venue">VenueEngineInitCallback</a> callback)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of existing SDKEngine.

    `callback` -

    The optional callback that will be triggered when a venue engine initialization will be completed. After the initialization, the <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">`VenueService`</a> should be started using one of its methods or using [](sdk-for-android-navigate-com-here-sdk-venue-venueengine#start(java.lang.String))

        start(String)

    </a>.

    </p>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-start-com-here-sdk-core-AuthenticationCallback" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationcallback" title="interface in com.here.sdk.core">AuthenticationCallback</a> callback)</span>

    </div>

    <div class="block">

    Authenticates asynchronously using HERE SDK credentials and uses a result token to start the VenueService . An initialization status of the venue service is returned to objects registered as VenueServiceListener . If the authentication will fail, the venue service will not be started.

    </div>

    Parameters:  
    `callback` -

    The optional callback that will be triggered when the authentication will be completed. If the authentication fails, the venue service will not be started.

    </div>

  - <div id="sdk-for-android-navigate-start-java-lang-String" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> token)</span>

    </div>

    <div class="block">

    Authenticates asynchronously using HERE SDK credentials using a token to start the VenueService . An initialization status of the venue service is returned to objects registered as VenueServiceListener . If the authentication will fail, the venue service will not be started.

    </div>

    Parameters:  
    `token` -

    SDK project scope token to be used for authentication

    </div>

  - <div id="sdk-for-android-navigate-destroy" class="section detail">

    ### destroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()

    </div>

    <div class="block">

    Releases all internally used resources. The instance can't be used anymore after calling this method.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getVenueService" class="section detail">

    ### getVenueService

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></span> <span class="element-name">getVenueService</span>()

    </div>

    <div class="block">

    Gets the venue service. This service can be used to load the venue model objects. Gets the VenueService . This service can be used to load the VenueModel objects.

    </div>

    Returns:  
    The venue service.

    </div>

  - <div id="sdk-for-android-navigate-getVenueMap" class="section detail">

    ### getVenueMap

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control">VenueMap</a></span> <span class="element-name">getVenueMap</span>()

    </div>

    <div class="block">

    Gets a venue map to visualize venues. Gets a venue map to visualize venues and control the state of the venues on the map. You need to start the VenueService to be able to load venues.

    </div>

    Returns:  
    The venue map.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

