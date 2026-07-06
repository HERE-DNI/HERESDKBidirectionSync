---
title: "SectionNotice (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-sectionnotice"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.SectionNotice

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">SectionNotice</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Explains an issue encountered in a Section .

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  [`SectionNoticeCode`](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnotice#code"
  class="member-name-link"><code>code</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The notice code.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`NoticeSeverity`](sdk-for-android-explore-com-here-sdk-routing-noticeseverity "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnotice#severity"
  class="member-name-link"><code>severity</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The notice severity.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`ViolatedRestriction`](sdk-for-android-explore-com-here-sdk-routing-violatedrestriction "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnotice#violatedRestrictions"
  class="member-name-link"><code>violatedRestrictions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The following property violated_restrictions contains the notice
  detail information.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      SectionNotice(SectionNoticeCode code,
       NoticeSeverity severity)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

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
<div id="sdk-for-android-explore-field-detail"
  class="section field-details">
<div id="sdk-for-android-explore-code" class="section detail">

    ### code

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">code</span>

    </div>

    <div class="block">

    The notice code.

    </div>

    </div>
<div id="sdk-for-android-explore-severity" class="section detail">

    ### severity

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[NoticeSeverity](sdk-for-android-explore-com-here-sdk-routing-noticeseverity "enum class in com.here.sdk.routing")</span> <span class="element-name">severity</span>

    </div>

    <div class="block">

    The notice severity.

    </div>

    </div>
<div id="sdk-for-android-explore-violatedRestrictions"
    class="section detail">

    ### violatedRestrictions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[ViolatedRestriction](sdk-for-android-explore-com-here-sdk-routing-violatedrestriction "class in com.here.sdk.routing")></span> <span class="element-name">violatedRestrictions</span>

    </div>

    <div class="block">

    The following property violated_restrictions contains the notice
    detail information. Only three types of restrictions can have notice
    details: time dependent restriction, vehicle restriction and
    transport mode restriction. There is no one-to-one match of the
    SectionNotice.code and these three restriction types. For example,
    if SectionNotice.code is
    SectionNoticeCode.VIOLATED_VEHICLE_RESTRICTION , then it can be
    either vehicle restriction or transport mode restriction. If
    SectionNotice.code is SectionNoticeCode.SEASONAL_CLOSURE , then it
    is time dependent restriction. If the section notice is none of the
    above-mentioned three types, then this will be an empty list.

    </div>

    </div>

  </div>
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>(com.here.sdk.routing.SectionNoticeCode,com.here.sdk.routing.NoticeSeverity)"
    class="section detail">

    ### SectionNotice

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SectionNotice</span><span class="parameters">(@NonNull
    [SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing") code,
    @NonNull
    [NoticeSeverity](sdk-for-android-explore-com-here-sdk-routing-noticeseverity "enum class in com.here.sdk.routing") severity)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `code` -

    The notice code.

    `severity` -

    The notice severity.

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

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
<div id="sdk-for-android-explore-hashCode()" class="section detail">

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

