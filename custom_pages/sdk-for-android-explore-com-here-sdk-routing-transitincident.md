---
title: "TransitIncident (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-transitincident"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.TransitIncident

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TransitIncident</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A transit incident describes disruptions on the transit network.
Disruptions scale from delays to service cancellations.

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
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#description"
  class="member-name-link"><code>description</code></a></td>
  <td><div class="block">
  A human readable description of the incident
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincidenteffect"
  title="enum class in com.here.sdk.routing"><code>TransitIncidentEffect</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#effect"
  class="member-name-link"><code>effect</code></a></td>
  <td><div class="block">
  Effect of the incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#summary"
  class="member-name-link"><code>summary</code></a></td>
  <td><div class="block">
  A human readable summary of the incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincidenttype"
  title="enum class in com.here.sdk.routing"><code>TransitIncidentType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#type"
  class="member-name-link"><code>type</code></a></td>
  <td><div class="block">
  Type of the incident.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#url"
  class="member-name-link"><code>url</code></a></td>
  <td><div class="block">
  Link to the original incident published at the agency website.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#validFrom"
  class="member-name-link"><code>validFrom</code></a></td>
  <td><div class="block">
  Valid from.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-transitincident#validUntil"
  class="member-name-link"><code>validUntil</code></a></td>
  <td><div class="block">
  Valid until.
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
  <td><pre><code>TransitIncident(String summary,
   String description,
   TransitIncidentType type,
   TransitIncidentEffect effect,
   Date validFrom,
   Date validUntil,
   String url)</code></pre></td>
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

  - <div id="summary" class="section detail">

    ### summary

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">summary</span>

    </div>

    <div class="block">

    A human readable summary of the incident.

    </div>

    </div>

  - <div id="description" class="section detail">

    ### description

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">description</span>

    </div>

    <div class="block">

    A human readable description of the incident

    </div>

    </div>

  - <div id="type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TransitIncidentType](sdk-for-android-explore-com-here-sdk-routing-transitincidenttype "enum class in com.here.sdk.routing")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Type of the incident.

    </div>

    </div>

  - <div id="effect" class="section detail">

    ### effect

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TransitIncidentEffect](sdk-for-android-explore-com-here-sdk-routing-transitincidenteffect "enum class in com.here.sdk.routing")</span> <span class="element-name">effect</span>

    </div>

    <div class="block">

    Effect of the incident.

    </div>

    </div>

  - <div id="validFrom" class="section detail">

    ### validFrom

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">validFrom</span>

    </div>

    <div class="block">

    Valid from.

    </div>

    </div>

  - <div id="validUntil" class="section detail">

    ### validUntil

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">validUntil</span>

    </div>

    <div class="block">

    Valid until.

    </div>

    </div>

  - <div id="url" class="section detail">

    ### url

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">url</span>

    </div>

    <div class="block">

    Link to the original incident published at the agency website.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.String,java.lang.String,com.here.sdk.routing.TransitIncidentType,com.here.sdk.routing.TransitIncidentEffect,java.util.Date,java.util.Date,java.lang.String)"
    class="section detail">

    ### TransitIncident

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransitIncident</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> summary,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> description,
    @Nullable
    [TransitIncidentType](sdk-for-android-explore-com-here-sdk-routing-transitincidenttype "enum class in com.here.sdk.routing") type,
    @Nullable
    [TransitIncidentEffect](sdk-for-android-explore-com-here-sdk-routing-transitincidenteffect "enum class in com.here.sdk.routing") effect,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a> validFrom,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a> validUntil,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> url)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `summary` -

    A human readable summary of the incident.

    `description` -

    A human readable description of the incident

    `type` -

    Type of the incident.

    `effect` -

    Effect of the incident.

    `validFrom` -

    Valid from.

    `validUntil` -

    Valid until.

    `url` -

    Link to the original incident published at the agency website.

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

