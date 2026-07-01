---
title: "IsolineOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-isolineoptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.IsolineOptions

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">IsolineOptions</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Specifies options for isolines calculation.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation"
  class="type-name-link"
  title="class in com.here.sdk.routing"><code>IsolineOptions.Calculation</code></a></td>
  <td><div class="block">
  Specifies isoline parameters.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation"
  title="class in com.here.sdk.routing"><code>IsolineOptions.Calculation</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions#calculationOptions"
  class="member-name-link"><code>calculationOptions</code></a></td>
  <td><div class="block">
  Specifies isoline parameters.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-caroptions"
  title="class in com.here.sdk.routing"><code>CarOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions#carOptions"
  class="member-name-link"><code>carOptions</code></a></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-evcaroptions"
  title="class in com.here.sdk.routing"><code>EVCarOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions#evCarOptions"
  class="member-name-link"><code>evCarOptions</code></a></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions"
  title="class in com.here.sdk.routing"><code>EVTruckOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions#evTruckOptions"
  class="member-name-link"><code>evTruckOptions</code></a></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routingoptions"
  title="class in com.here.sdk.routing"><code>RoutingOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions#routingOptions"
  class="member-name-link"><code>routingOptions</code></a></td>
  <td><div class="block">
  Specifies options for calculation of isolines for any vehicle type.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-truckoptions"
  title="class in com.here.sdk.routing"><code>TruckOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions#truckOptions"
  class="member-name-link"><code>truckOptions</code></a></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><pre><code>IsolineOptions(IsolineOptions.Calculation calculationOptions,
   CarOptions carOptions)</code></pre></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineOptions(IsolineOptions.Calculation calculationOptions,
   EVCarOptions evCarOptions)</code></pre></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineOptions(IsolineOptions.Calculation calculationOptions,
   EVTruckOptions evTruckOptions)</code></pre></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineOptions(IsolineOptions.Calculation calculationOptions,
   RoutingOptions routingOptions)</code></pre></td>
  <td><div class="block">
  Constructs options to calculate isolines from destination or origin,
  with preferences for isoline calculation and routing options.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>IsolineOptions(IsolineOptions.Calculation calculationOptions,
   TruckOptions truckOptions)</code></pre></td>
  <td><div class="block">
  Deprecated. Will be removed in v4.28.0.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

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

- <div id="field-detail" class="section field-details">

  - <div id="calculationOptions" class="section detail">

    ### calculationOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[IsolineOptions.Calculation](sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation "class in com.here.sdk.routing")</span> <span class="element-name">calculationOptions</span>

    </div>

    <div class="block">

    Specifies isoline parameters.

    </div>

    </div>

  - <div id="carOptions" class="section detail">

    ### carOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a> @Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing")</span> <span class="element-name">carOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the `routing_options` instead.

    </div>

    </div>

    <div class="block">

    Specifies options for calculation of isolines for car. Mutually
    exclusive with truckOptions , evCarOptions , evTruckOptions and
    routingOptions .

    </div>

    </div>

  - <div id="truckOptions" class="section detail">

    ### truckOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a> @Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing")</span> <span class="element-name">truckOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the `routing_options` instead.

    </div>

    </div>

    <div class="block">

    Specifies options for calculation of isolines for truck. Mutually
    exclusive with carOptions , evCarOptions , evTruckOptions and
    routingOptions .

    </div>

    </div>

  - <div id="evCarOptions" class="section detail">

    ### evCarOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a> @Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing")</span> <span class="element-name">evCarOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the `routing_options` instead.

    </div>

    </div>

    <div class="block">

    Specifies options for calculation of isolines for electric car.
    Mutually exclusive with carOptions , truckOptions , evTruckOptions
    and routingOptions .

    </div>

    </div>

  - <div id="evTruckOptions" class="section detail">

    ### evTruckOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a> @Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing")</span> <span class="element-name">evTruckOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the `routing_options` instead.

    </div>

    </div>

    <div class="block">

    Specifies options for calculation of isolines for electric truck.
    Mutually exclusive with carOptions , truckOptions , evCarOptions and
    routingOptions .

    </div>

    </div>

  - <div id="routingOptions" class="section detail">

    ### routingOptions

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing")</span> <span class="element-name">routingOptions</span>

    </div>

    <div class="block">

    Specifies options for calculation of isolines for any vehicle type.
    Mutually exclusive with carOptions , truckOptions , evCarOptions and
    evTruckOptions .

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.CarOptions)"
    class="section detail">

    ### IsolineOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a>
    </span><span class="modifiers">public</span> <span class="element-name">IsolineOptions</span><span class="parameters">(@NonNull
    [IsolineOptions.Calculation](sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation "class in com.here.sdk.routing") calculationOptions,
    @NonNull
    [CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing") carOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the constructor with
    `RoutingOptions` parameter instead.

    </div>

    </div>

    <div class="block">

    Constructs options to calculate isolines from destination or origin,
    with preferences for isoline calculation and car routing options.

    </div>

    Parameters:  
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `carOptions` -

    The options that should influence the possible routes within the
    isoline. This determines also the transportation type.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.TruckOptions)"
    class="section detail">

    ### IsolineOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a>
    </span><span class="modifiers">public</span> <span class="element-name">IsolineOptions</span><span class="parameters">(@NonNull
    [IsolineOptions.Calculation](sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation "class in com.here.sdk.routing") calculationOptions,
    @NonNull
    [TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing") truckOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the constructor with
    `RoutingOptions` parameter instead.

    </div>

    </div>

    <div class="block">

    Constructs options to calculate isolines from destination or origin,
    with preferences for isoline calculation and truck routing options.

    </div>

    Parameters:  
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `truckOptions` -

    The options that should influence the possible routes within the
    isoline. This determines also the transportation type.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVCarOptions)"
    class="section detail">

    ### IsolineOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a>
    </span><span class="modifiers">public</span> <span class="element-name">IsolineOptions</span><span class="parameters">(@NonNull
    [IsolineOptions.Calculation](sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation "class in com.here.sdk.routing") calculationOptions,
    @NonNull
    [EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing") evCarOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the constructor with
    `RoutingOptions` parameter instead.

    </div>

    </div>

    <div class="block">

    Constructs options to calculate isolines from destination or origin,
    with preferences for isoline calculation and electric car routing
    options.

    </div>

    Parameters:  
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `evCarOptions` -

    The options that should influence the possible routes within the
    isoline. This determines also the transportation type.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVTruckOptions)"
    class="section detail">

    ### IsolineOptions

    <div class="member-signature">

    <span class="annotations"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
    class="external-link"
    title="class or interface in java.lang">@Deprecated</a>
    </span><span class="modifiers">public</span> <span class="element-name">IsolineOptions</span><span class="parameters">(@NonNull
    [IsolineOptions.Calculation](sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation "class in com.here.sdk.routing") calculationOptions,
    @NonNull
    [EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing") evTruckOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the constructor with
    `RoutingOptions` parameter instead.

    </div>

    </div>

    <div class="block">

    Constructs options to calculate isolines from destination or origin,
    with preferences for isoline calculation and electric truck routing
    options.

    </div>

    Parameters:  
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `evTruckOptions` -

    The options that should influence the possible routes within the
    isoline. This determines also the transportation type.

    </div>

  - <div id="<init>(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.RoutingOptions)"
    class="section detail">

    ### IsolineOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IsolineOptions</span><span class="parameters">(@NonNull
    [IsolineOptions.Calculation](sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation "class in com.here.sdk.routing") calculationOptions,
    @NonNull
    [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") routingOptions)</span>

    </div>

    <div class="block">

    Constructs options to calculate isolines from destination or origin,
    with preferences for isoline calculation and routing options. Notes
    By default all vehicle specifications from
    RoutingOptions.transportSpecification are set to null and the
    TransportSpecification.transportMode from
    RoutingOptions.transportSpecification is set to TransportMode.CAR .
    A route can be calculated with only the
    TransportSpecification.transportMode from
    RoutingOptions.transportSpecification set.

    </div>

    Parameters:  
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `routingOptions` -

    The options that should influence the possible routes within the
    isoline. This determines also the transportation type.

    </div>

  </div>

</div>

