---
title: "TollFare (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-tollfare"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.TollFare → com.here.sdk.routing.TollFare

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TollFare</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This struct presents all the fare data for a toll. Note : If you're using the OfflineRoutingEngine , be aware that this feature is currently in beta . As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the OfflineRoutingEngine is only available for the Navigate license. If you're using the RoutingEngine , this feature is considered to be stable.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#currency" class="member-name-link"><code>currency</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The currency in which the toll is to be paid in ISO 4217 format, e.g.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">`TollFarePass`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#pass" class="member-name-link"><code>pass</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies whether this TollFare is a multi-travel pass, and its characteristics.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">`PaymentMethod`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#paymentMethods" class="member-name-link"><code>paymentMethods</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of accepted payment methods like cash and credit card.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#price" class="member-name-link"><code>price</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The amount of the toll be paid.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">`TimeRule`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#timeRule" class="member-name-link"><code>timeRule</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The time domain when this fare is valid.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare#transponders" class="member-name-link"><code>transponders</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of available transponders.

  </div>

  </div>

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

      TollFare ( String currency,
       double price, List < PaymentMethod > paymentMethods)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      TollFare ( String currency,
       double price, List < PaymentMethod > paymentMethods, TimeRule timeRule)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      TollFare ( String currency,
       double price, List < PaymentMethod > paymentMethods, TimeRule timeRule, List < String > transponders)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      TollFare ( String currency,
       double price, List < PaymentMethod > paymentMethods, TimeRule timeRule, List < String > transponders, TollFarePass pass)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

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

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-currency" class="section detail">

    ### currency

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">currency</span>

    </div>

    <div class="block">

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    </div>

    </div>

  - <div id="sdk-for-android-navigate-price" class="section detail">

    ### price

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">price</span>

    </div>

    <div class="block">

    The amount of the toll be paid.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-paymentMethods" class="section detail">

    ### paymentMethods

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>\></span> <span class="element-name">paymentMethods</span>

    </div>

    <div class="block">

    The list of accepted payment methods like cash and credit card.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timeRule" class="section detail">

    ### timeRule

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span>

    </div>

    <div class="block">

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the Time Domain

    </div>

    </div>

  - <div id="sdk-for-android-navigate-transponders" class="section detail">

    ### transponders

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\></span> <span class="element-name">transponders</span>

    </div>

    <div class="block">

    The list of available transponders.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-pass" class="section detail">

    ### pass

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a></span> <span class="element-name">pass</span>

    </div>

    <div class="block">

    Specifies whether this TollFare is a multi-travel pass, and its characteristics.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-lang-String-double-java-util-List" class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> currency, double price, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>\> paymentMethods)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String-double-java-util-List-com-here-sdk-core-TimeRule" class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> currency, double price, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>\> paymentMethods, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String-double-java-util-List-com-here-sdk-core-TimeRule-java-util-List" class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> currency, double price, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>\> paymentMethods, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\> transponders)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>

    `transponders` -

    The list of available transponders.

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String-double-java-util-List-com-here-sdk-core-TimeRule-java-util-List-com-here-sdk-routing-TollFarePass" class="section detail">

    ### TollFare

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TollFare</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> currency, double price, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a>\> paymentMethods, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a> timeRule, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\> transponders, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a> pass)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `currency` -

    The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".

    `price` -

    The amount of the toll be paid.

    `paymentMethods` -

    The list of accepted payment methods like cash and credit card.

    `timeRule` -

    The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>

    `transponders` -

    The list of available transponders.

    `pass` -

    Specifies whether this <a href="sdk-for-android-navigate-com-here-sdk-routing-tollfare" title="class in com.here.sdk.routing">`TollFare`</a> is a multi-travel pass, and its characteristics.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

