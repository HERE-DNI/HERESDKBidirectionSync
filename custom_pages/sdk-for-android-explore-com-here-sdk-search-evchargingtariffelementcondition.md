---
title: "EVChargingTariffElementCondition (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evchargingtariffelementcondition"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.EVChargingTariffElementCondition

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVChargingTariffElementCondition</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Condition that the charging session needs to meet to apply the tariff
element. Tariff elements may include conditions that define when they
apply: Time of day (e.g., 22:00–06:00) Day of week (e.g., weekends only)
Date range (e.g., seasonal pricing) Charging session duration Battery
level thresholds (e.g., overstay fees) Note: This is a beta release of
this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-search-daterange"
  title="class in com.here.sdk.search"><code>DateRange</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtariffelementcondition#date"
  class="member-name-link"><code>date</code></a></td>
  <td><div class="block">
  Date range when the tariff element is valid.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-dayofweek"
  title="enum class in com.here.sdk.search"><code>DayOfWeek</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtariffelementcondition#days"
  class="member-name-link"><code>days</code></a></td>
  <td><div class="block">
  Day(s) of the week when the tariff element is valid.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingdurationrange"
  title="class in com.here.sdk.search"><code>EVChargingDurationRange</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtariffelementcondition#duration"
  class="member-name-link"><code>duration</code></a></td>
  <td><div class="block">
  Duration of the charging session when the tariff element is valid, in
  seconds.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtariffelementcondition#overstayBatteryLevel"
  class="member-name-link"><code>overstayBatteryLevel</code></a></td>
  <td><div class="block">
  Minimum battery level when the tariff element is valid, in percentages.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-timeofdayrange"
  title="class in com.here.sdk.search"><code>TimeOfDayRange</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtariffelementcondition#time"
  class="member-name-link"><code>time</code></a></td>
  <td><div class="block">
  Time period when the tariff element is valid, in local time.
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
  <td><pre><code>EVChargingTariffElementCondition()</code></pre></td>
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

  - <div id="date" class="section detail">

    ### date

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[DateRange](sdk-for-android-explore-com-here-sdk-search-daterange "class in com.here.sdk.search")</span> <span class="element-name">date</span>

    </div>

    <div class="block">

    Date range when the tariff element is valid. This is typically used
    to indicate seasonal tariffs or to announce an update to the tariff
    in advance. It may also be used to indicate spot prices, together
    with time period.

    </div>

    </div>

  - <div id="days" class="section detail">

    ### days

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[DayOfWeek](sdk-for-android-explore-com-here-sdk-search-dayofweek "enum class in com.here.sdk.search")></span> <span class="element-name">days</span>

    </div>

    <div class="block">

    Day(s) of the week when the tariff element is valid. An example
    would be to specify lower prices for weekends

    </div>

    </div>

  - <div id="time" class="section detail">

    ### time

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TimeOfDayRange](sdk-for-android-explore-com-here-sdk-search-timeofdayrange "class in com.here.sdk.search")</span> <span class="element-name">time</span>

    </div>

    <div class="block">

    Time period when the tariff element is valid, in local time. The
    time period wraps around to the next day, when end time of the
    period TimeOfDayRange.to is smaller than the beginning
    TimeOfDayRange.from .

    </div>

    </div>

  - <div id="duration" class="section detail">

    ### duration

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingDurationRange](sdk-for-android-explore-com-here-sdk-search-evchargingdurationrange "class in com.here.sdk.search")</span> <span class="element-name">duration</span>

    </div>

    <div class="block">

    Duration of the charging session when the tariff element is valid,
    in seconds. Often only either one of the values is present,
    indicating the minimum or maximum duration.

    </div>

    </div>

  - <div id="overstayBatteryLevel" class="section detail">

    ### overstayBatteryLevel

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">overstayBatteryLevel</span>

    </div>

    <div class="block">

    Minimum battery level when the tariff element is valid, in
    percentages. This can be used to set additional fees for charging a
    full or nearly full battery.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### EVChargingTariffElementCondition

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVChargingTariffElementCondition</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

