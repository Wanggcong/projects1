function Histogram_Equalization()
    close all 
    fi=imread('Fig3.08(a).jpg');
    figure,imshow(fi),title('ԭʼͼ��')
    
    [m,n]=size(fi);
    Pr=zeros(1,256); 
    for k=0:255 
        Pr(k+1)=length(find(fi==k))/(m*n);  %ͳ�ƻҶ�ֵΪk�����صĳ��ָ���
    end 
                   
    figure(1),bar(0:255,Pr,'k'),title('ԭʼͼ��ֱ��ͼ')
    xlabel('�Ҷ�ֵ'),ylabel('���ָ���');     %��ӡԭʼͼ��ֱ��ͼ
    saveas(1,'oringin_hist.jpg');
    
    sumPr=zeros(1,256); 
    for i=1:256 
        for j=1:i 
            sumPr(i)=Pr(j)*255+sumPr(i);      %���⻯��������ÿ���Ҷ�i��ͻҶ�0~i�ĸ���
        end 
    end 
    
    figure(2),plot(0:255,sumPr,'k'),title('���⻯����')
    xlabel('�Ҷ�ֵ'),ylabel('���ָ���');   %��ӡ���⻯����
    saveas(2,'eq_plot.jpg');
    
    newGray=round((sumPr)+0.5);       %��ÿ���Ҷȵĸ������Ӧ���µĻҶ�ֵ����������
    for i=1:256 
        Ps(i)=sum(Pr(newGray==i));        %ps(i)��ʾ�Ҷ�Ϊi�����س��ֵĸ���
    end 
    
    figure(3),bar(0:255,Ps,'k'),title('���⻯���ֱ��ͼ')
    xlabel('�Ҷ�ֵ'),ylabel('���ָ���');   %��ӡ���⻯���ֱ��ͼ
    saveas(3,'new_hist.jpg');
    
    fiEq=fi; 
    for i=0:255 
        fiEq(fi==i)=newGray(i+1);         %��fi�лҶ�Ϊi�����ؿ��滻ΪnewGray�е��»Ҷ�
    end 
    figure,imshow(fiEq),title('���⻯��ͼ��');
    imwrite(fiEq,'Fig3.08(a)Eq.jpg'); 