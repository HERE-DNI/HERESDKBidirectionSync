---
title: "TransitDeparture (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-transitdeparture"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.TransitDeparture → com.here.sdk.routing.TransitDeparture

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TransitDeparture</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

This struct holds the transit departure or arrival information.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitdeparture#delay" class="member-name-link"><code>delay</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The accumulated delay in seconds from the scheduled time of the event.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`RoutePlace`](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitdeparture#place" class="member-name-link"><code>place</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The departure or arrival place.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TransitDepartureStatus`](sdk-for-android-explore-com-here-sdk-routing-transitdeparturestatus "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitdeparture#status" class="member-name-link"><code>status</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Status of the departure.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-transitdeparture#time" class="member-name-link"><code>time</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Expected departure or arrival time of the event.

  </div>

  </div>

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

      TransitDeparture ( RoutePlace place, Date time, Integer delay, TransitDepartureStatus status)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-place" class="section detail">

    ### place

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")</span> <span class="element-name">place</span>

    </div>

    <div class="block">

    The departure or arrival place.

    </div>

    </div>

  - <div id="sdk-for-android-explore-time" class="section detail">

    ### time

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">time</span>

    </div>

    <div class="block">

    Expected departure or arrival time of the event.

    </div>

    </div>

  - <div id="sdk-for-android-explore-delay" class="section detail">

    ### delay

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">delay</span>

    </div>

    <div class="block">

    The accumulated delay in seconds from the scheduled time of the event.

    </div>

    </div>

  - <div id="sdk-for-android-explore-status" class="section detail">

    ### status

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[TransitDepartureStatus](sdk-for-android-explore-com-here-sdk-routing-transitdeparturestatus "enum class in com.here.sdk.routing")</span> <span class="element-name">status</span>

    </div>

    <div class="block">

    Status of the departure.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-RoutePlace-java-util-Date-java-lang-Integer-com-here-sdk-routing-TransitDepartureStatus" class="section detail">

    ### TransitDeparture

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransitDeparture</span><wbr></wbr><span class="parameters">(@NonNull [RoutePlace](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing") place, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> time, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> delay, @Nullable [TransitDepartureStatus](sdk-for-android-explore-com-here-sdk-routing-transitdeparturestatus "enum class in com.here.sdk.routing") status)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `place` -

    The departure or arrival place.

    `time` -

    Expected departure or arrival time of the event.

    `delay` -

    The accumulated delay in seconds from the scheduled time of the event.

    `status` -

    Status of the departure.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

