---
title: "Address (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-address"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.Address

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Address</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Information about the address of a location. Used in Place.getAddress()
. Note that while OfflineSearchEngine.suggest and
OfflineSearchEngine.suggestByText set all available details,
SearchEngine.suggest and SearchEngine.suggestByText set only addressText
. Complete address details can be obtained by searching with
PlaceIdQuery .

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
  href="sdk-for-android-explore-com-here-sdk-search-address#addressText"
  class="member-name-link"><code>addressText</code></a></td>
  <td><div class="block">
  The text for the address, for example, "Secret Garden, 347 Lewis Ave,
  Brooklyn, NY 11233, United States".
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address#block"
  class="member-name-link"><code>block</code></a></td>
  <td><div class="block">
  The block number for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address#city"
  class="member-name-link"><code>city</code></a></td>
  <td><div class="block">
  The city name for the address, for example, "Brooklyn".
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#country"
  class="member-name-link"><code>country</code></a></td>
  <td><div class="block">
  The country name for the address, for example, "United States".
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#countryCode"
  class="member-name-link"><code>countryCode</code></a></td>
  <td><div class="block">
  An ISO-3166-1 (3-letter) country code for the address, for example,
  "USA".
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address#county"
  class="member-name-link"><code>county</code></a></td>
  <td><div class="block">
  The county name for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#district"
  class="member-name-link"><code>district</code></a></td>
  <td><div class="block">
  The district name for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#houseNumOrName"
  class="member-name-link"><code>houseNumOrName</code></a></td>
  <td><div class="block">
  The house name or number for the address, for example, "347".
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#postalCode"
  class="member-name-link"><code>postalCode</code></a></td>
  <td><div class="block">
  The postal code for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address#state"
  class="member-name-link"><code>state</code></a></td>
  <td><div class="block">
  The state name for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#stateCode"
  class="member-name-link"><code>stateCode</code></a></td>
  <td><div class="block">
  The state code for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address#street"
  class="member-name-link"><code>street</code></a></td>
  <td><div class="block">
  The street name for the address, for example, "Lewis Ave".
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#subBlock"
  class="member-name-link"><code>subBlock</code></a></td>
  <td><div class="block">
  The sub-block number for the address.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-address#subdistrict"
  class="member-name-link"><code>subdistrict</code></a></td>
  <td><div class="block">
  The subdistrict name for the address.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-addresstype"
  title="enum class in com.here.sdk.search"><code>AddressType</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address#type"
  class="member-name-link"><code>type</code></a></td>
  <td><div class="block">
  Specifies the address type.
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
  <td><pre><code>Address()</code></pre></td>
  <td><div class="block">
  Default constructor.
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

  - <div id="city" class="section detail">

    ### city

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">city</span>

    </div>

    <div class="block">

    The city name for the address, for example, "Brooklyn". Note: This
    String can be empty when no data is available.

    </div>

    </div>

  - <div id="countryCode" class="section detail">

    ### countryCode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">countryCode</span>

    </div>

    <div class="block">

    An ISO-3166-1 (3-letter) country code for the address, for example,
    "USA". Note: This String can be empty when no data is available.

    </div>

    </div>

  - <div id="country" class="section detail">

    ### country

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">country</span>

    </div>

    <div class="block">

    The country name for the address, for example, "United States".
    Note: This String can be empty when no data is available.

    </div>

    </div>

  - <div id="district" class="section detail">

    ### district

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">district</span>

    </div>

    <div class="block">

    The district name for the address. It is a division of city,
    typically an administrative unit within a larger city or a customary
    name of a city's neighborhood, for example, "Bedford-Stuyvesant".
    Note: This String can be empty when no data is available.

    </div>

    </div>

  - <div id="subdistrict" class="section detail">

    ### subdistrict

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">subdistrict</span>

    </div>

    <div class="block">

    The subdistrict name for the address. It is a subdivision of a
    district. Note: This String can be empty when no data is available.

    </div>

    </div>

  - <div id="houseNumOrName" class="section detail">

    ### houseNumOrName

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">houseNumOrName</span>

    </div>

    <div class="block">

    The house name or number for the address, for example, "347". Note:
    This String can be empty when no data is available.

    </div>

    </div>

  - <div id="postalCode" class="section detail">

    ### postalCode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">postalCode</span>

    </div>

    <div class="block">

    The postal code for the address. It is an alphanumeric string
    included in a postal address to facilitate mail sorting, known
    locally in various countries throughout the world as a postcode,
    post code, PIN or ZIP Code, for example, "11233". Note: This String
    can be empty when no data is available.

    </div>

    </div>

  - <div id="state" class="section detail">

    ### state

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">state</span>

    </div>

    <div class="block">

    The state name for the address. It is the name of the state division
    of a country, for example, "New York". Note: This String can be
    empty when no data is available.

    </div>

    </div>

  - <div id="county" class="section detail">

    ### county

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">county</span>

    </div>

    <div class="block">

    The county name for the address. It is a division of a state,
    typically a secondary-level administrative division of a country or
    equivalent, for example, "Kings". Note: This String can be empty
    when no data is available.

    </div>

    </div>

  - <div id="street" class="section detail">

    ### street

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">street</span>

    </div>

    <div class="block">

    The street name for the address, for example, "Lewis Ave". Note:
    This String can be empty when no data is available.

    </div>

    </div>

  - <div id="block" class="section detail">

    ### block

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">block</span>

    </div>

    <div class="block">

    The block number for the address. It is part of Japanese addressing
    system. Note: This String can be empty when no data is available.

    </div>

    </div>

  - <div id="subBlock" class="section detail">

    ### subBlock

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">subBlock</span>

    </div>

    <div class="block">

    The sub-block number for the address. It is part of Japanese
    addressing system. Note: This String can be empty when no data is
    available.

    </div>

    </div>

  - <div id="addressText" class="section detail">

    ### addressText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">addressText</span>

    </div>

    <div class="block">

    The text for the address, for example, "Secret Garden, 347 Lewis
    Ave, Brooklyn, NY 11233, United States". Note: This String can be
    empty when no data is available.

    </div>

    </div>

  - <div id="type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[AddressType](sdk-for-android-explore-com-here-sdk-search-addresstype "enum class in com.here.sdk.search")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Specifies the address type.

    </div>

    </div>

  - <div id="stateCode" class="section detail">

    ### stateCode

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">stateCode</span>

    </div>

    <div class="block">

    The state code for the address. It is code/abbreviation of the state
    division of a country, for example, "NY". Note: This String can be
    empty when no data is available.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### Address

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Address</span>()

    </div>

    <div class="block">

    Default constructor. Note: Sets all the string values to "".

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

