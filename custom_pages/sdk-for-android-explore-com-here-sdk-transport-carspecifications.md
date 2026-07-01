---
title: "CarSpecifications (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-transport-carspecifications"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.transport](sdk-for-android-explore-com-here-sdk-transport-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.transport.CarSpecifications

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
class="external-link"
title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class
</span><span class="element-name type-name-label">CarSpecifications</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="deprecation-block">

<span class="deprecated-label">Deprecated.</span>

<div class="deprecation-comment">

Will be removed in v4.28.0. Use `TransportSpecification` instead.

</div>

</div>

<div class="block">

Car specifications contain vehicle related attributes. Examples:
Dimensions, weight, axle count. Only the fields that are set are
considered for restriction handling.

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#axleCount"
  class="member-name-link"><code>axleCount</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Defines total number of axles in the vehicle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#grossWeightInKilograms"
  class="member-name-link"><code>grossWeightInKilograms</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Car weight including trailers and shipped goods in kilograms.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#heightInCentimeters"
  class="member-name-link"><code>heightInCentimeters</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Car height in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#lengthInCentimeters"
  class="member-name-link"><code>lengthInCentimeters</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Car length in centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#trailerAxleCount"
  class="member-name-link"><code>trailerAxleCount</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Defines total number of axles across all the trailers attached to the
  vehicle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#trailerCount"
  class="member-name-link"><code>trailerCount</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Defines number of trailers attached to the vehicle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-carspecifications#widthInCentimeters"
  class="member-name-link"><code>widthInCentimeters</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Car width in centimeters.
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
  <td><pre><code>CarSpecifications()</code></pre></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
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
  Deprecated Methods

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
  <td><div class="block">
  Deprecated.
  </div>
   </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td><div class="block">
  Deprecated.
  </div>
   </td>
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

  - <div id="grossWeightInKilograms" class="section detail">

    ### grossWeightInKilograms

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">grossWeightInKilograms</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Car weight including trailers and shipped goods in kilograms. The
    provided value must be greater than or equal to 0. By default, it is
    not set. Note: This parameter is limited to a maximum weight of 4250
    kg without trailer and 7550 kg with trailer.

    </div>

    </div>

  - <div id="heightInCentimeters" class="section detail">

    ### heightInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">heightInCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Car height in centimeters. The provided value must be in the range
    \[0, 5000\]. By default, it is not set.

    </div>

    </div>

  - <div id="widthInCentimeters" class="section detail">

    ### widthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">widthInCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Car width in centimeters. The provided value must be in the range
    \[0, 5000\]. By default, it is not set.

    </div>

    </div>

  - <div id="lengthInCentimeters" class="section detail">

    ### lengthInCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">lengthInCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Car length in centimeters. The provided value must be in the range
    \[0, 30000\]. By default, it is not set.

    </div>

    </div>

  - <div id="axleCount" class="section detail">

    ### axleCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">axleCount</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines total number of axles in the vehicle. The provided value
    must be greater than or equal to 2. By default, it is not set. Route
    calculation: When not set, possible axle count restrictions will not
    be taken into consideration. When specifying trailerAxleCount , then
    axleCount is required and must be greater than trailerAxleCount .

    </div>

    </div>

  - <div id="trailerCount" class="section detail">

    ### trailerCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerCount</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines number of trailers attached to the vehicle. The provided
    value must be in the range \[0, 1\]. By default, it is not set. When
    specifying trailerAxleCount , then trailerCount is required and must
    be greater than 0.

    </div>

    </div>

  - <div id="trailerAxleCount" class="section detail">

    ### trailerAxleCount

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">trailerAxleCount</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Defines total number of axles across all the trailers attached to
    the vehicle. This number is included in axleCount , hence
    trailerAxleCount must be less than axleCount and greater than or
    equal to 1. axleCount and trailerCount are required to specify
    trailerAxleCount . By default, it is not set.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### CarSpecifications

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CarSpecifications</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

