---
title: "TollFare (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-tollfare"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.TollFare

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TollFare</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This struct presents all the fare data for a toll. Note : If you're
using the OfflineRoutingEngine , be aware that this feature is currently
in beta . As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future
releases without going through the deprecation process. Note that the
OfflineRoutingEngine is only available for the Navigate license. If
you're using the RoutingEngine , this feature is considered to be
stable.

</div>

</div>

<div class="section summary">

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-tollfare#currency"
  class="member-name-link"><code>currency</code></a></td>
  <td><div class="block">
  The currency in which the toll is to be paid in ISO 4217 format, e.g.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-tollfarepass"
  title="class in com.here.sdk.routing"><code>TollFarePass</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-tollfare#pass"
  class="member-name-link"><code>pass</code></a></td>
  <td><div class="block">
  Specifies whether this TollFare is a multi-travel pass, and its
  characteristics.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-paymentmethod"
  title="enum class in com.here.sdk.routing"><code>PaymentMethod</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-tollfare#paymentMethods"
  class="member-name-link"><code>paymentMethods</code></a></td>
  <td><div class="block">
  The list of accepted payment methods like cash and credit card.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-tollfare#price"
  class="member-name-link"><code>price</code></a></td>
  <td><div class="block">
  The amount of the toll be paid.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-timerule"
  title="class in com.here.sdk.core"><code>TimeRule</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-tollfare#timeRule"
  class="member-name-link"><code>timeRule</code></a></td>
  <td><div class="block">
  The time domain when this fare is valid.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-tollfare#transponders"
  class="member-name-link"><code>transponders</code></a></td>
  <td><div class="block">
  The list of available transponders.
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
  <td><pre><code>TollFare(String currency,
   double price,
   List&lt;PaymentMethod&gt; paymentMethods)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>TollFare(String currency,
   double price,
   List&lt;PaymentMethod&gt; paymentMethods,
   TimeRule timeRule)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>TollFare(String currency,
   double price,
   List&lt;PaymentMethod&gt; paymentMethods,
   TimeRule timeRule,
   List&lt;String&gt; transponders)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>TollFare(String currency,
   double price,
   List&lt;PaymentMethod&gt; paymentMethods,
   TimeRule timeRule,
   List&lt;String&gt; transponders,
   TollFarePass pass)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
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
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
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

  - <div id="currency" class="section detail">

    ### currency

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">currency</span>

    </div>

    <div class="block">

    The currency in which the toll is to be paid in ISO 4217 format,
    e.g. "USD".

    </div>

    </div>

  - <div id="price" class="section detail">

    ### price

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">price</span>

    </div>

    <div class="block">

    The amount of the toll be paid.

    </div>

    </div>

  - <div id="paymentMethods" class="section detail">

    ### paymentMethods

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PaymentMethod](sdk-for-android-explore-com-here-sdk-routing-paymentmethod "enum class in com.here.sdk.routing")></span> <span class="element-name">paymentMethods</span>

    </div>

    <div class="block">

    The list of accepted payment methods like cash and credit card.

    </div>

    </div>

  - <div id="timeRule" class="section detail">

    ### timeRule

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TimeRule](sdk-for-android-explore-com-here-sdk-core-timerule "class in com.here.sdk.core")</span> <span class="element-name">timeRule</span>

    </div>

    <div class="block">

    The time domain when this fare is valid. If this field is missing,
    it means the fare is always valid. For a detailed description of the
    Time Domain specification and usage in routing services, please
    refer to the documentation available in the Time Domain

    </div>

    </div>

  - <div id="transponders" class="section detail">

    ### transponders

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>></span> <span class="element-name">transponders</span>

    </div>

    <div class="block">

    The list of available transponders.

    </div>

    </div>

  - <div id="pass" class="section detail">

    ### pass

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TollFarePass](sdk-for-android-explore-com-here-sdk-routing-tollfarepass "class in com.here.sdk.routing")</span> <span class="element-name">pass</span>

    </div>

    <div class="block">

    Specifies whether this TollFare is a multi-travel pass, and its
    characteristics.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.String,double,java.util.List)"
    class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> currency,
    double price, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PaymentMethod](sdk-for-android-explore-com-here-sdk-routing-paymentmethod "enum class in com.here.sdk.routing")> paymentMethods)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format,
    e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    </div>

  - <div id="<init>(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule)"
    class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> currency,
    double price, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PaymentMethod](sdk-for-android-explore-com-here-sdk-routing-paymentmethod "enum class in com.here.sdk.routing")> paymentMethods,
    @Nullable
    [TimeRule](sdk-for-android-explore-com-here-sdk-core-timerule "class in com.here.sdk.core") timeRule)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format,
    e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing,
    it means the fare is always valid. For a detailed description of the
    Time Domain specification and usage in routing services, please
    refer to the documentation available in the [Time
    Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)

    </div>

  - <div id="<init>(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List)"
    class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> currency,
    double price, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PaymentMethod](sdk-for-android-explore-com-here-sdk-routing-paymentmethod "enum class in com.here.sdk.routing")> paymentMethods,
    @Nullable
    [TimeRule](sdk-for-android-explore-com-here-sdk-core-timerule "class in com.here.sdk.core") timeRule,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> transponders)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format,
    e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing,
    it means the fare is always valid. For a detailed description of the
    Time Domain specification and usage in routing services, please
    refer to the documentation available in the [Time
    Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)

    `transponders` -

    The list of available transponders.

    </div>

  - <div id="<init>(java.lang.String,double,java.util.List,com.here.sdk.core.TimeRule,java.util.List,com.here.sdk.routing.TollFarePass)"
    class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> currency,
    double price, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PaymentMethod](sdk-for-android-explore-com-here-sdk-routing-paymentmethod "enum class in com.here.sdk.routing")> paymentMethods,
    @Nullable
    [TimeRule](sdk-for-android-explore-com-here-sdk-core-timerule "class in com.here.sdk.core") timeRule,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> transponders,
    @Nullable
    [TollFarePass](sdk-for-android-explore-com-here-sdk-routing-tollfarepass "class in com.here.sdk.routing") pass)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format,
    e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing,
    it means the fare is always valid. For a detailed description of the
    Time Domain specification and usage in routing services, please
    refer to the documentation available in the [Time
    Domain](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html)

    `transponders` -

    The list of available transponders.

    `pass` -

    Specifies whether this
    [`TollFare`](sdk-for-android-explore-com-here-sdk-routing-tollfare "class in com.here.sdk.routing")
    is a multi-travel pass, and its characteristics.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

