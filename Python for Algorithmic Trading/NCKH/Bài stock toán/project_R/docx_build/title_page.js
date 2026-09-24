const fs=require('fs');const {Document,Packer,Paragraph,TextRun,AlignmentType,HeadingLevel}=require('docx');
const P=(t,o={})=>new Paragraph({spacing:{after:160},...o,children:[].concat(t)});
const R=(t,o={})=>new TextRun({text:t,font:'Times New Roman',size:24,...o});
const H=(t)=>new TextRun({text:t,font:'Times New Roman',size:24,highlight:'yellow'});
const doc=new Document({sections:[{properties:{page:{size:{width:11906,height:16838}}},children:[
 P(R('Title page',{bold:true,size:28}),{alignment:AlignmentType.CENTER}),
 P(R('Nested Equity Index Correlations Overstate True Co-Movement: Evidence from Vietnam',{bold:true}),{alignment:AlignmentType.CENTER}),
 P([R('Authors: ',{bold:true}),H('[Full names of all authors, in order]')]),
 P([R('Affiliations and addresses: ',{bold:true}),H('[Institution, department, postal address for each author]')]),
 P([R('Corresponding author: ',{bold:true}),H('[Name; e-mail; telephone]')]),
 P([R('JEL classification: ',{bold:true}),R('C58, G11, G12')]),
 P([R('Author contributions (CRediT): ',{bold:true}),H('[e.g., A: Conceptualization, Methodology, Software, Formal analysis, Writing – original draft; B: Supervision, Writing – review & editing]')]),
 P([R('Funding: ',{bold:true}),H('[Funding organization written in full and grant number, or: "This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors."]')]),
 P([R('Acknowledgments: ',{bold:true}),H('[Optional: people or institutions to thank]')]),
 P([R('Conflict of interest: ',{bold:true}),R('The authors declare that they have no conflict of interest.')]),
]}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync(process.argv[2],b));
