---
title: "UsageStats (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-usagestats"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.engine.UsageStats → com.here.sdk.core.engine.UsageStats

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">UsageStats</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature" class="type-name-link" title="enum class in com.here.sdk.core.engine"><code>UsageStats.Feature</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents the feature enum associated with the gathered usage stats.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats" class="type-name-link" title="class in com.here.sdk.core.engine"><code>UsageStats.NetworkStats</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Provides network statistics in bytes per method.

  </div>

  </div>

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

  [`UsageStats.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats#feature" class="member-name-link"><code>feature</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents the HERE SDK feature associated with the gathered usage statistics.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`UsageStats.NetworkStats`](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats "class in com.here.sdk.core.engine")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats#networkStats" class="member-name-link"><code>networkStats</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Provides network statistics.

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

      UsageStats ( List < UsageStats.NetworkStats > networkStats, UsageStats.Feature feature)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-networkStats" class="section detail">

    ### networkStats

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[UsageStats.NetworkStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats "class in com.here.sdk.core.engine")\></span> <span class="element-name">networkStats</span>

    </div>

    <div class="block">

    Provides network statistics.

    </div>

    </div>

  - <div id="sdk-for-android-explore-feature" class="section detail">

    ### feature

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">feature</span>

    </div>

    <div class="block">

    Represents the HERE SDK feature associated with the gathered usage statistics.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-java-util-List-com-here-sdk-core-engine-UsageStats-Feature" class="section detail">

    ### UsageStats

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">UsageStats</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[UsageStats.NetworkStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-networkstats "class in com.here.sdk.core.engine")\> networkStats, @NonNull [UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine") feature)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `networkStats` -

    Provides network statistics.

    `feature` -

    Represents the HERE SDK feature associated with the gathered usage statistics.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

