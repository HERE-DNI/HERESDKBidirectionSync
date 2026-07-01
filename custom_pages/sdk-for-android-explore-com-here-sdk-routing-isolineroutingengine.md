---
title: "IsolineRoutingEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-isolineroutingengine"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.routing.IsolineRoutingEngine →
com.here.NativeBase → com.here.sdk.routing.IsolineRoutingEngine

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">IsolineRoutingEngine</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Use the IsolineRoutingEngine to calculate a reachable area from a center
point. The calculation is done asynchronously and requires an online
connection.

</div>

</div>

<div class="section summary">

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>IsolineRoutingEngine()</code></pre></td>
  <td><div class="block">
  Creates a new instance of this class.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineRoutingEngine(SDKNativeEngine sdkEngine)</code></pre></td>
  <td><div class="block">
  Creates a new instance of IsolineRoutingEngine.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineRoutingEngine(SDKNativeEngine sdkEngine,
   RoutingConnectionSettings connectionSettings)</code></pre></td>
  <td><div class="block">
  Creates a new instance of RoutingEngine.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineRoutingEngine(RoutingConnectionSettings connectionSettings)</code></pre></td>
  <td><div class="block">
  Creates a new instance of RoutingEngine.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-threading-taskhandle"
  title="interface in com.here.sdk.core.threading"><code>TaskHandle</code></a></td>
  <td><pre><code>calculateIsoline(Waypoint center,
   IsolineOptions isolineOptions,
   CalculateIsolineCallback callback)</code></pre></td>
  <td><div class="block">
  Asynchronously calculates isolines to indicate the reachable area from a
  center point.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-routingerror"
  title="enum class in com.here.sdk.routing"><code>RoutingError</code></a></td>
  <td><pre><code>setCustomOption(String name,
   String value)</code></pre></td>
  <td><div class="block">
  Sets a custom option for routing backend queries.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span>()
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="<init>(com.here.sdk.routing.RoutingConnectionSettings)"
    class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><span class="parameters">(@NonNull
    [RoutingConnectionSettings](sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings "class in com.here.sdk.routing") connectionSettings)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of RoutingEngine.

    </div>

    Parameters:  
    `connectionSettings` -

    Settings for the route calculation.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="<init>(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)"
    class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine,
    @NonNull
    [RoutingConnectionSettings](sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings "class in com.here.sdk.routing") connectionSettings)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

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
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="<init>(com.here.sdk.core.engine.SDKNativeEngine)"
    class="section detail">

    ### IsolineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineRoutingEngine</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of IsolineRoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="calculateIsoline(com.here.sdk.routing.Waypoint,com.here.sdk.routing.IsolineOptions,com.here.sdk.routing.CalculateIsolineCallback)"
    class="section detail">

    ### calculateIsoline

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateIsoline</span><span class="parameters">(@NonNull
    [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") center,
    @NonNull
    [IsolineOptions](sdk-for-android-explore-com-here-sdk-routing-isolineoptions "class in com.here.sdk.routing") isolineOptions,
    @NonNull
    [CalculateIsolineCallback](sdk-for-android-explore-com-here-sdk-routing-calculateisolinecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates isolines to indicate the reachable area
    from a center point. This finds all destinations that can be reached
    in a specific amount of time, a maximum travel distance, or even the
    charge level available in an electric vehicle. The result is a
    polygon area where each point is reachable within the provided
    limit.

    </div>

    Parameters:  
    `center` -

    Center point from which isolines are calculated. At minimum, the
    waypoint must contain the coordinates as point of origin.

    `isolineOptions` -

    Options for isoline calculation.

    `callback` -

    Callback object that will be invoked after isoline calculation. It
    is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="setCustomOption(java.lang.String,java.lang.String)"
    class="section detail">

    ### setCustomOption

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">setCustomOption</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets a custom option for routing backend queries. The custom option
    is applied to all the queries that IsolineRoutingEngine performs.
    For a complete list of available parameter names and their valid
    values, refer to HERE Routing API v8 . Note: It's easy to set a
    wrong option that makes queries invalid, so make sure you read and
    understand the backend documentation.

    </div>

    Parameters:  
    `name` -

    An option name. If the engine already has an option with the same
    name, the option will be overwritten. The option name must be a
    non-empty string. The option name should't duplicate option names
    that SDK creates by itself for usage in the query, otherwise the
    query will callback with the error `RoutingError.INTERNAL_ERROR`.

    `value` -

    An option value. If the value is `null`, the option will be removed.
    The option value must be a non-empty string.

    Returns:  
    An optional error of setting the option. It's `null` if the option
    has been set successfully. It's `RoutingError.INVALID_PARAMETER` if
    the input name and/or value haven't passed internal validation.

    </div>

  </div>

</div>

