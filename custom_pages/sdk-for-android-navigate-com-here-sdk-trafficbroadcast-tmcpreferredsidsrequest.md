---
title: "TMCPreferredSidsRequest (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcpreferredsidsrequest"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-package-summary">com.here.sdk.trafficbroadcast</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.trafficbroadcast.TMCPreferredSidsRequest → com.here.sdk.trafficbroadcast.TMCPreferredSidsRequest

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TMCPreferredSidsRequest</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents data used to request the list of preferred SIDs.

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

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcpreferredsidsrequest#countryCode" class="member-name-link"><code>countryCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Refers to a country in RDS-TMC format.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `short`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcpreferredsidsrequest#ltn" class="member-name-link"><code>ltn</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  LTN to which the requested SIDs belong.

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

      TMCPreferredSidsRequest (short countryCode,
       short ltn)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-countryCode" class="section detail">

    ### countryCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">countryCode</span>

    </div>

    <div class="block">

    Refers to a country in RDS-TMC format.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-ltn" class="section detail">

    ### ltn

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">ltn</span>

    </div>

    <div class="block">

    LTN to which the requested SIDs belong.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-short-short" class="section detail">

    ### TMCPreferredSidsRequest

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TMCPreferredSidsRequest</span><wbr></wbr><span class="parameters">(short countryCode, short ltn)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `countryCode` -

    Refers to a country in RDS-TMC format.

    `ltn` -

    LTN to which the requested SIDs belong.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

