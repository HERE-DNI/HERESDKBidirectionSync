---
title: "TransitSectionDetails (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.TransitSectionDetails

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TransitSectionDetails</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Gives the details of a transit section.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-agency"
  title="class in com.here.sdk.routing"><code>Agency</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails#agency"
  class="member-name-link"><code>agency</code></a></td>
  <td><div class="block">
  Contains information about a particular agency.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-attribution"
  title="class in com.here.sdk.routing"><code>Attribution</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails#attributions"
  class="member-name-link"><code>attributions</code></a></td>
  <td><div class="block">
  List of required attributions to display.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-fare"
  title="class in com.here.sdk.routing"><code>Fare</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails#fares"
  class="member-name-link"><code>fares</code></a></td>
  <td><div class="block">
  List of tickets to pay for this section of the route.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident"
  title="class in com.here.sdk.routing"><code>TransitIncident</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails#incidents"
  class="member-name-link"><code>incidents</code></a></td>
  <td><div class="block">
  A list of all incidents that apply to the section.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitstop"
  title="class in com.here.sdk.routing"><code>TransitStop</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails#intermediateStops"
  class="member-name-link"><code>intermediateStops</code></a></td>
  <td><div class="block">
  All the intermediate stops between departure and destination of this
  section.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transittransport"
  title="class in com.here.sdk.routing"><code>TransitTransport</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails#transport"
  class="member-name-link"><code>transport</code></a></td>
  <td><div class="block">
  Transit transport information.
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
  <td><pre><code>TransitSectionDetails(Agency agency)</code></pre></td>
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

  - <div id="transport" class="section detail">

    ### transport

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TransitTransport](sdk-for-android-explore-com-here-sdk-routing-transittransport "class in com.here.sdk.routing")</span> <span class="element-name">transport</span>

    </div>

    <div class="block">

    Transit transport information.

    </div>

    </div>

  - <div id="intermediateStops" class="section detail">

    ### intermediateStops

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[TransitStop](sdk-for-android-explore-com-here-sdk-routing-transitstop "class in com.here.sdk.routing")></span> <span class="element-name">intermediateStops</span>

    </div>

    <div class="block">

    All the intermediate stops between departure and destination of this
    section.

    </div>

    </div>

  - <div id="agency" class="section detail">

    ### agency

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Agency](sdk-for-android-explore-com-here-sdk-routing-agency "class in com.here.sdk.routing")</span> <span class="element-name">agency</span>

    </div>

    <div class="block">

    Contains information about a particular agency.

    </div>

    </div>

  - <div id="attributions" class="section detail">

    ### attributions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[Attribution](sdk-for-android-explore-com-here-sdk-routing-attribution "class in com.here.sdk.routing")></span> <span class="element-name">attributions</span>

    </div>

    <div class="block">

    List of required attributions to display.

    </div>

    </div>

  - <div id="fares" class="section detail">

    ### fares

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[Fare](sdk-for-android-explore-com-here-sdk-routing-fare "class in com.here.sdk.routing")></span> <span class="element-name">fares</span>

    </div>

    <div class="block">

    List of tickets to pay for this section of the route. Note:
    Currently, fare information is not supported and the list will be
    always empty.

    </div>

    </div>

  - <div id="incidents" class="section detail">

    ### incidents

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[TransitIncident](sdk-for-android-explore-com-here-sdk-routing-transitincident "class in com.here.sdk.routing")></span> <span class="element-name">incidents</span>

    </div>

    <div class="block">

    A list of all incidents that apply to the section.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.routing.Agency)"
    class="section detail">

    ### TransitSectionDetails

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransitSectionDetails</span><span class="parameters">(@NonNull
    [Agency](sdk-for-android-explore-com-here-sdk-routing-agency "class in com.here.sdk.routing") agency)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `agency` -

    Contains information about a particular agency.

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

