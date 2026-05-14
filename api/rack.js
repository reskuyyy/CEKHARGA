export default async function handler(req,res){

  const {
    storeId,
    rack
  } = req.query;

  const url =
  `https://app.alfastore.co.id/prd/api/mob/tablet/productinfo/CheckPerRack/?storeId=${storeId}&rack=${rack}`;

  try{

    const response =
    await fetch(url);

    const data =
    await response.json();

    res.status(200).json(data);

  }catch(err){

    res.status(500).json({
      error:'Gagal fetch API'
    });

  }

}
