---
title: "PlaceCategory Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-placecategory"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PlaceCategory.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PlaceCategory"></a>
<a title="PlaceCategory Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PlaceCategory Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PlaceCategory</code></pre>
<pre><code>extension PlaceCategory: NativeBase</code></pre>
<pre><code>extension PlaceCategory: Hashable</code></pre>
</div>
</div>
<p>Represents a category of place with different levels of granularity.
This class also defines a set of most commonly used categories.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC2idACSS_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:)"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC2idACSS_tcfc">init(id:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(id: String)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>id</em>
</code>
</td>
<td>
<div>
<p>Place category ID.
The HERE places category system provides three levels of granularity:

<ol>
<li>Level 1 represents high level groupings, such as “Eat and drink”.
Their IDs take the form “xxx”, for example “100”.</li>
<li>Level 2 represents logical sub-groups or domains, such as “Eat and Drink / Restaurant”.
Their IDs take the form “xxx-xxxx”, for example “100-1000”.</li>
<li>Level 3 provides the greatest level of granularity about place categorization,
such as “Eat and Drink / Restaurant / Casual Dining”.
Their IDs take the form “xxx-xxxx-xxxx”, for example “100-1000-0001”.
The category ID can be provided as one of the predefined values, such as
<code><a href="../Classes/PlaceCategory.html#/s:7heresdk13PlaceCategoryC21eatAndDrinkRestaurantSSvpZ">PlaceCategory.eatAndDrinkRestaurant</a></code> or as a literal string that matches
one of the category IDs defined by the HERE Search service.
Only level 1 and 2 category IDs are predefined.
The complete list of supported category IDs, including level 3, can be found online:
<a href="https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html">https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html</a>.</li>
</ol></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC11eatAndDrinkSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/eatAndDrink"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC11eatAndDrinkSSvpZ">eatAndDrink</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places where food or beverages are prepared or served.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let eatAndDrink: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC21eatAndDrinkRestaurantSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/eatAndDrinkRestaurant"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC21eatAndDrinkRestaurantSSvpZ">eatAndDrinkRestaurant</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment that prepares and serves refreshments and prepared meals.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let eatAndDrinkRestaurant: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC20eatAndDrinkCoffeeTeaSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/eatAndDrinkCoffeeTea"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC20eatAndDrinkCoffeeTeaSSvpZ">eatAndDrinkCoffeeTea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment that sells drinks, such as coffee and tea, as well as refreshments.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let eatAndDrinkCoffeeTea: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC21goingOutEntertainmentSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/goingOutEntertainment"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC21goingOutEntertainmentSSvpZ">goingOutEntertainment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places commonly associated with entertainment,
such as bars, cinemas, theatres, casinos and night clubs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let goingOutEntertainment: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17goingOutNightlifeSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/goingOutNightlife"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17goingOutNightlifeSSvpZ">goingOutNightlife</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment that provides evening entertainment and usually serves alcoholic beverages.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let goingOutNightlife: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC14goingOutCinemaSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/goingOutCinema"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC14goingOutCinemaSSvpZ">goingOutCinema</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment that shows movies through screen projection.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let goingOutCinema: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC27goingOutTheatreMusicCultureSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/goingOutTheatreMusicCulture"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC27goingOutTheatreMusicCultureSSvpZ">goingOutTheatreMusicCulture</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment where various types of performing arts are presented.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let goingOutTheatreMusicCulture: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC30goingOutGamblingLotteryBettingSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/goingOutGamblingLotteryBetting"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC30goingOutGamblingLotteryBettingSSvpZ">goingOutGamblingLotteryBetting</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment that provides gambling entertainment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let goingOutGamblingLotteryBetting: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC16sightsAndMuseumsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/sightsAndMuseums"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC16sightsAndMuseumsSSvpZ">sightsAndMuseums</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places of special interest,
such as common tourist attractions, museums and places of worship.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let sightsAndMuseums: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC24sightsLandmarkAttractionSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/sightsLandmarkAttraction"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC24sightsLandmarkAttractionSSvpZ">sightsLandmarkAttraction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A designated area of special interest to tourists.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let sightsLandmarkAttraction: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC12sightsMuseumSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/sightsMuseum"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC12sightsMuseumSSvpZ">sightsMuseum</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let sightsMuseum: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC015sightsReligiousB0SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/sightsReligiousPlace"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC015sightsReligiousB0SSvpZ">sightsReligiousPlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment special religious significance or where religious services are held.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let sightsReligiousPlace: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC22naturalAndGeographicalSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/naturalAndGeographical"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC22naturalAndGeographicalSSvpZ">naturalAndGeographical</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for natural or man-made areas of regional importance,
such as bodies of water, mountains, forested areas and other geographic areas.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let naturalAndGeographical: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC33naturalAndGeographicalBodyOfWaterSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/naturalAndGeographicalBodyOfWater"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC33naturalAndGeographicalBodyOfWaterSSvpZ">naturalAndGeographicalBodyOfWater</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A natural and geographical feature of the earth’s surface that is covered with water, such as a lake, river, stream or ocean.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let naturalAndGeographicalBodyOfWater: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC36naturalAndGeographicalMountainOrHillSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/naturalAndGeographicalMountainOrHill"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC36naturalAndGeographicalMountainOrHillSSvpZ">naturalAndGeographicalMountainOrHill</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A natural and geographical feature that is higher than the surrounding land.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let naturalAndGeographicalMountainOrHill: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC37naturalAndGeographicalUnderseaFeatureSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/naturalAndGeographicalUnderseaFeature"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC37naturalAndGeographicalUnderseaFeatureSSvpZ">naturalAndGeographicalUnderseaFeature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A natural or artificial feature that is below sea level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let naturalAndGeographicalUnderseaFeature: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC49naturalAndGeographicalForestHealthOtherVegetationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/naturalAndGeographicalForestHealthOtherVegetation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC49naturalAndGeographicalForestHealthOtherVegetationSSvpZ">naturalAndGeographicalForestHealthOtherVegetation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A dense growth of trees, open uncultivated land or other large masses of vegetation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let naturalAndGeographicalForestHealthOtherVegetation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC27naturalAndGeographicalOtherSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/naturalAndGeographicalOther"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC27naturalAndGeographicalOtherSSvpZ">naturalAndGeographicalOther</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let naturalAndGeographicalOther: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC9transportSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/transport"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC9transportSSvpZ">transport</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places commonly associated with pedestrian and cargo transport facilities,
including airports, rail yards and seaports.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let transport: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC16transportAirportSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/transportAirport"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC16transportAirportSSvpZ">transportAirport</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let transportAirport: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC15transportPublicSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/transportPublic"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC15transportPublicSSvpZ">transportPublic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A facility for travelers who are travelling between stops on public transport.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let transportPublic: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC14transportCargoSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/transportCargo"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC14transportCargoSSvpZ">transportCargo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A facility that handles some aspect of the transportation of cargo freight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let transportCargo: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17transportRestAreaSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/transportRestArea"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17transportRestAreaSSvpZ">transportRestArea</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment along a motorway (controlled access road) that provides restrooms and parking.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let transportRestArea: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC13accommodationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/accommodation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC13accommodationSSvpZ">accommodation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers,
such as hotels, motels, resorts, cruise ships and campgrounds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let accommodation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC23accommodationHotelMotelSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/accommodationHotelMotel"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC23accommodationHotelMotelSSvpZ">accommodationHotelMotel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that provides lodging or temporary living quarters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let accommodationHotelMotel: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC20accommodationLodgingSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/accommodationLodging"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC20accommodationLodgingSSvpZ">accommodationLodging</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that provides lodging to the public generally without room service.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let accommodationLodging: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17leisureAndOutdoorSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/leisureAndOutdoor"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17leisureAndOutdoorSSvpZ">leisureAndOutdoor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places that are designated for sports, recreation, parking, beaches
and other leisure and outdoor activities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let leisureAndOutdoor: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC24leisureOutdoorRecreationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/leisureOutdoorRecreation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC24leisureOutdoorRecreationSSvpZ">leisureOutdoorRecreation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Public land preserved and maintained for recreational use.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let leisureOutdoorRecreation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC12leisureOtherSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/leisureOther"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC12leisureOtherSSvpZ">leisureOther</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A park that contains rides and/or other entertainment which may be based on a central theme.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let leisureOther: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC8shoppingSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shopping"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC8shoppingSSvpZ">shopping</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places where consumer goods are commonly sold,
such as clothing stores, grocery stores, hardware stores and other types of shopping centers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shopping: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC24shoppingConvenienceStoreSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingConvenienceStore"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC24shoppingConvenienceStoreSSvpZ">shoppingConvenienceStore</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingConvenienceStore: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC19shoppingMallComplexSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingMallComplex"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC19shoppingMallComplexSSvpZ">shoppingMallComplex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A complex of businesses that are co-located and share common services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingMallComplex: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC23shoppingDepartmentStoreSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingDepartmentStore"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC23shoppingDepartmentStoreSSvpZ">shoppingDepartmentStore</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells a wide variety of merchandise that is organized by product or service departments.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingDepartmentStore: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC20shoppingFoodAndDrinkSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingFoodAndDrink"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC20shoppingFoodAndDrinkSSvpZ">shoppingFoodAndDrink</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells specialty products of a particular type of food or beverage.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingFoodAndDrink: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC25shoppingDrugstorePharmacySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingDrugstorePharmacy"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC25shoppingDrugstorePharmacySSvpZ">shoppingDrugstorePharmacy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells medications, toiletry items and other retail cosmetics.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingDrugstorePharmacy: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC19shoppingElectronicsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingElectronics"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC19shoppingElectronicsSSvpZ">shoppingElectronics</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells consumer electronics and electronic entertainment equipment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingElectronics: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC27shoppingHardwareHouseGardenSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingHardwareHouseGarden"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC27shoppingHardwareHouseGardenSSvpZ">shoppingHardwareHouseGarden</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells crafts, gardening, remodeling, or decorating items for the home.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingHardwareHouseGarden: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17shoppingBookstoreSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingBookstore"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17shoppingBookstoreSSvpZ">shoppingBookstore</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells books, magazines and other reading material.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingBookstore: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC29shoppingClothingAndAccesoriesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingClothingAndAccesories"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC29shoppingClothingAndAccesoriesSSvpZ">shoppingClothingAndAccesories</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells apparel items, garments or fashion accessories for men, women, and children.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingClothingAndAccesories: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC21shoppingConsumerGoodsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingConsumerGoods"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC21shoppingConsumerGoodsSSvpZ">shoppingConsumerGoods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that sells a variety of products targeted to consumers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingConsumerGoods: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC21shoppingHairAndBeautySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shoppingHairAndBeauty"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC21shoppingHairAndBeautySSvpZ">shoppingHairAndBeauty</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A business that provides hair styling and personal appearance services.
Places in this category may also sell hair products and other related cosmetic items.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shoppingHairAndBeauty: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC19businessAndServicesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServices"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC19businessAndServicesSSvpZ">businessAndServices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places that provide professional services to other businesses,
such as printing, photocopying, graphic design, marketing, advertising and other general business services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServices: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC26businessAndServicesBankingSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesBanking"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC26businessAndServicesBankingSSvpZ">businessAndServicesBanking</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that specialize in the maintenance, lending, exchange, or issuance of money.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesBanking: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC22businessAndServicesAtmSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesAtm"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC22businessAndServicesAtmSSvpZ">businessAndServicesAtm</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesAtm: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC28businessAndServicesMoneyCashSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesMoneyCash"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC28businessAndServicesMoneyCashSSvpZ">businessAndServicesMoneyCash</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that provide money related services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesMoneyCash: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC37businessAndServicesCommunicationMediaSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesCommunicationMedia"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC37businessAndServicesCommunicationMediaSSvpZ">businessAndServicesCommunicationMedia</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that provide communication services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesCommunicationMedia: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC29businessAndCommercialServicesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndCommercialServices"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC29businessAndCommercialServicesSSvpZ">businessAndCommercialServices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that provide a service or product for use by other businesses.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndCommercialServices: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC27businessAndServicesIndustrySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesIndustry"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC27businessAndServicesIndustrySSvpZ">businessAndServicesIndustry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that employ people in and around the city in which it is located.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesIndustry: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC38businessAndServicesPoliceFireEmergencySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesPoliceFireEmergency"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC38businessAndServicesPoliceFireEmergencySSvpZ">businessAndServicesPoliceFireEmergency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Municipal emergency services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesPoliceFireEmergency: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC27businessAndConsumerServicesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndConsumerServices"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC27businessAndConsumerServicesSSvpZ">businessAndConsumerServices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An organization that provides consumer services for a variety of products for used by the public.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndConsumerServices: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC29businessAndServicesPostOfficeSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesPostOffice"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC29businessAndServicesPostOfficeSSvpZ">businessAndServicesPostOffice</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesPostOffice: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC37businessAndServicesTouristInformationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesTouristInformation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC37businessAndServicesTouristInformationSSvpZ">businessAndServicesTouristInformation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that provide a variety of information for visiting tourists,
such as event schedules, lodging/accommodations, restaurants, attractions and more.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesTouristInformation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC33businessAndServicesFuelingStationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesFuelingStation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC33businessAndServicesFuelingStationSSvpZ">businessAndServicesFuelingStation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that sell fuel for vehicles, such as petrol, electricity etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesFuelingStation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesPetrolGasolineStation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">businessAndServicesPetrolGasolineStation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that sell fuel, oil, and other motoring supplies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesPetrolGasolineStation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesEvChargingStation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">businessAndServicesEvChargingStation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that provide recharging services for electric vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesEvChargingStation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC33businessAndServicesCarDealerSalesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesCarDealerSales"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC33businessAndServicesCarDealerSalesSSvpZ">businessAndServicesCarDealerSales</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that sell new automobiles and motorcycles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesCarDealerSales: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC028businessAndServicesCarRepairF0SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesCarRepairServices"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC028businessAndServicesCarRepairF0SSvpZ">businessAndServicesCarRepairServices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that provide automotive repair services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesCarRepairServices: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC28businessAndServicesCarRentalSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesCarRental"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC28businessAndServicesCarRentalSSvpZ">businessAndServicesCarRental</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Businesses that rent or lease automobiles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesCarRental: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC34businessAndServicesTruckSemiDealerSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/businessAndServicesTruckSemiDealer"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC34businessAndServicesTruckSemiDealerSSvpZ">businessAndServicesTruckSemiDealer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Business that sell or service trucks and tractor trailers.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let businessAndServicesTruckSemiDealer: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC10facilitiesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilities"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC10facilitiesSSvpZ">facilities</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places associated with specialized facilities,
such as sports venues, government buildings, health care centers and other types of facilities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilities: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC28facilitiesHospitalHealthcareSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesHospitalHealthcare"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC28facilitiesHospitalHealthcareSSvpZ">facilitiesHospitalHealthcare</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Facilities that include dental offices, hospitals, nursing homes and other health care-related services.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesHospitalHealthcare: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC30facilitiesGovernmentCommunittySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesGovernmentCommunitty"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC30facilitiesGovernmentCommunittySSvpZ">facilitiesGovernmentCommunitty</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A Place where government services are provided.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesGovernmentCommunitty: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC19facilitiesEducationSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesEducation"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC19facilitiesEducationSSvpZ">facilitiesEducation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Facilities that are used for educational purposes including training, coaching, universities and more.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesEducation: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC16facilitiesSchoolSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesSchool"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC16facilitiesSchoolSSvpZ">facilitiesSchool</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Educational facilities that include primary schools, secondary schools and more.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesSchool: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17facilitiesLibrarySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesLibrary"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17facilitiesLibrarySSvpZ">facilitiesLibrary</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Facilities that offer books, periodicals, audio, video and other material for public use.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesLibrary: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC21facilitiesEventSpacesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesEventSpaces"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC21facilitiesEventSpacesSSvpZ">facilitiesEventSpaces</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An area or facility used for the hosting of fairs and conventions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesEventSpaces: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17facilitiesParkingSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesParking"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17facilitiesParkingSSvpZ">facilitiesParking</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Area or building used for parking cars.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesParking: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC21facilitiesVenueSportsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesVenueSports"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC21facilitiesVenueSportsSSvpZ">facilitiesVenueSports</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A facility used for individual and team sports including recreational sports.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesVenueSports: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC15facilitiesOtherSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/facilitiesOther"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC15facilitiesOtherSSvpZ">facilitiesOther</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let facilitiesOther: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC17areasAndBuildingsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/areasAndBuildings"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC17areasAndBuildingsSSvpZ">areasAndBuildings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Top level category for places that are owned, operated or managed by municipalities,
such as cities, towns, villages, boroughs and shires.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let areasAndBuildings: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC31areasAndBuildingsOutdoorComplexSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/areasAndBuildingsOutdoorComplex"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC31areasAndBuildingsOutdoorComplexSSvpZ">areasAndBuildingsOutdoorComplex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Outdoor areas or complexes with designations for specific businesses or interests.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let areasAndBuildingsOutdoorComplex: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC33areasAndBuildingsResidentalOfficeSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/areasAndBuildingsResidentalOffice"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC33areasAndBuildingsResidentalOfficeSSvpZ">areasAndBuildingsResidentalOffice</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Areas and buildings designated for residential or office use.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let areasAndBuildingsResidentalOffice: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC2idSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC2idSSvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Place category ID.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var id: String { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13PlaceCategoryC4nameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk13PlaceCategoryC4nameSSSgvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Localised place category name.
It is available only when when <code>PlaceCategory</code> is obtained from <code><a href="../Classes/Place.html">Place</a></code>.
That means that when <code>PlaceCategory</code> is constructed directly by the client,
<code>name</code> is always <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var name: String? { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
