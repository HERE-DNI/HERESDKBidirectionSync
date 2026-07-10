---
title: "IsolineRoutingEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-isolineroutingengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.IsolineRoutingEngine → com.here.NativeBase com.here.sdk.routing.IsolineRoutingEngine → com.here.sdk.routing.IsolineRoutingEngine

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">IsolineRoutingEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Use the IsolineRoutingEngine to calculate a reachable area from a center point. The calculation is done asynchronously and requires an online connection.

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

      IsolineRoutingEngine ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      IsolineRoutingEngine ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of IsolineRoutingEngine.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      IsolineRoutingEngine ( SDKNativeEngine sdkEngine, RoutingConnectionSettings connectionSettings)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of RoutingEngine.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      IsolineRoutingEngine ( RoutingConnectionSettings connectionSettings)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of RoutingEngine.

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

  <a href="sdk-for-android-explore-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      calculateIsoline ( Waypoint center, IsolineOptions isolineOptions, CalculateIsolineCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates isolines to indicate the reachable area from a center point.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">`RoutingError`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomOption ( String name, String value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom option for routing backend queries.

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

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span>() throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-RoutingConnectionSettings" class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</span> throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of RoutingEngine.

    </div>

    Parameters:  
    `connectionSettings` -

    Settings for the route calculation.

    Throws:  
    <a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-routing-RoutingConnectionSettings" class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</span> throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of RoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    `connectionSettings` -

    Settings for the route calculation.

    Throws:  
    <a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of IsolineRoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    <a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-calculateIsoline-com-here-sdk-routing-Waypoint-com-here-sdk-routing-IsolineOptions-com-here-sdk-routing-CalculateIsolineCallback" class="section detail">

    ### calculateIsoline

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateIsoline</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a> center, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions" title="class in com.here.sdk.routing">IsolineOptions</a> isolineOptions, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-calculateisolinecallback" title="interface in com.here.sdk.routing">CalculateIsolineCallback</a> callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates isolines to indicate the reachable area from a center point. This finds all destinations that can be reached in a specific amount of time, a maximum travel distance, or even the charge level available in an electric vehicle. The result is a polygon area where each point is reachable within the provided limit.

    </div>

    Parameters:  
    `center` -

    Center point from which isolines are calculated. At minimum, the waypoint must contain the coordinates as point of origin.

    `isolineOptions` -

    Options for isoline calculation.

    `callback` -

    Callback object that will be invoked after isoline calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-setCustomOption-java-lang-String-java-lang-String" class="section detail">

    ### setCustomOption

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">setCustomOption</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets a custom option for routing backend queries. The custom option is applied to all the queries that IsolineRoutingEngine performs. For a complete list of available parameter names and their valid values, refer to HERE Routing API v8 . Note: It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

    </div>

    Parameters:  
    `name` -

    An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string. The option name should't duplicate option names that SDK creates by itself for usage in the query, otherwise the query will callback with the error `RoutingError.INTERNAL_ERROR`.

    `value` -

    An option value. If the value is `null`, the option will be removed. The option value must be a non-empty string.

    Returns:  
    An optional error of setting the option. It's `null` if the option has been set successfully. It's `RoutingError.INVALID_PARAMETER` if the input name and/or value haven't passed internal validation.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

